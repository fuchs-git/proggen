import math
from datetime import datetime
import psycopg

import psycopg
from psycopg import DatabaseError


class Datenpunkt:
    def __init__(self, zeit: datetime, lat: float, lon: float):
        self.zeit = zeit
        self.lat = lat
        self.lon = lon

    def __eq__(self, other: "Datenpunkt"):
        return self.zeit == other.zeit

    def __hash__(self):
        return hash(self.zeit)

    def __lt__(self, other: "Datenpunkt"):
        return self.zeit < other.zeit

    def abstand(self, other: "Datenpunkt"):
        return (math.sqrt((self.lat - other.lat) ** 2
                          + (self.lon - other.lon) ** 2)
                * 40000 / 360)


# Teil der Schiffsdaten
class Schiff:
    def __init__(self, mmsi, name, typ):
        self.mmsi = mmsi
        self.name = name
        self.typ = typ
        self.datenpunkte = set()

    def __str__(self):
        return f"{self.name} ({self.mmsi}) [{self.typ}]"

    def datenpunkt_hinzufuegen(self, zeit: datetime, lat: float, lon: float):
        self.datenpunkte.add(Datenpunkt(zeit, lat, lon))

    def fahrstrecke(self):
        pkt_chronologisch = sorted(self.datenpunkte)
        abstand = 0
        pkt_a = pkt_chronologisch[0]
        for pkt_b in pkt_chronologisch[1:]:
            abstand += pkt_a.abstand(pkt_b)
            pkt_a = pkt_b

        return abstand

    def __lt__(self, other):
        return self.name < other.name


class Datenbank:
    def __init__(self, password: str, setup=False):
        self.config_setup = {'user': 'postgres',
                             'password': password,
                             'dbname': 'postgres',
                             'host': 'localhost',
                             'port': 5432,
                             'autocommit': True}
        self.config_ais = {'user': 'postgres',
                           'password': password,
                           'dbname': 'prg_ais',
                           'host': 'localhost',
                           'port': 5432,
                           'autocommit': True}

        if setup: self.erstelle_db()

    def erstelle_db(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_setup) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('''DROP DATABASE IF EXISTS prg_ais''')
                    cursor.execute('''CREATE DATABASE prg_ais''')
        except psycopg.DatabaseError as e:
            print(e, type(e))

        try:
            with psycopg.connect(**self.config_ais) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('''CREATE TABLE vessel
                                      (
                                          mmsi INT PRIMARY KEY,
                                          name TEXT,
                                          typ  TEXT
                                      )''')
                    cursor.execute('''CREATE TABLE aisdata
                                      (
                                          mmsi         INT REFERENCES vessel (mmsi),
                                          basedatetime TIMESTAMP,
                                          lat          DECIMAL,
                                          lon          DECIMAL,
                                          PRIMARY KEY (mmsi, basedatetime)
                                      )''')
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def muster(self):
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('''''')
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def csv_einlesen(self, data):
        # print('MMSI,BaseDateTime,LAT,LON,SOG,COG,Heading,VesselName,IMO,CallSign,VesselType,Status,Length,Width,Draft,Cargo,TransceiverClass'.lower())
        # mmsi,basedatetime,lat,lon,sog,cog,heading,vesselname,imo,callsign,vesseltype,status,length,width,draft,cargo,transceiverclass
        schiffe = {}
        schiff_set = set()
        datenpunkt_set = set()
        try:
            with open(data) as f:
                f.readline()  # erste Zeile weglassen (Header)
                for zeile in f:

                    # MM, Time, LAT, LON, S, C, H, Name, I, C, Typ, S, Length, Width,Draft,Cargo,TransceiverClass
                    mmsi, zeit, lat, lon, _, _, _, name, _, _, typ, *_ = zeile.split(",")

                    if mmsi not in schiffe:
                        # Es gibt Zeilen in denen der Typ kaputt ist
                        typ = int(typ) if typ else 99
                        # ----------------------------------------------------------------------------
                        # Beim Datenbank lesen
                        schiff_set.add((mmsi, name, schiffstypen[typ]))

                        # ----------------------------------------------------------------------------

                    datenpunkt_set.add((mmsi, datetime.strptime(zeit, "%Y-%m-%dT%H:%M:%S"), float(lat),
                                        float(lon)))
        except FileNotFoundError:
            print(f"Datei {data} nicht gefunden")

        except OSError:
            print(f"Fehler beim Lesen der Datei {data}")

        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_ais) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.executemany('''INSERT INTO vessel (mmsi, name, typ)
                                          VALUES (%s, %s, %s)''', schiff_set)
                    cursor.executemany('''INSERT INTO aisdata (mmsi, basedatetime, lat, lon)
                                          VALUES (%s, %s, %s, %s)''', datenpunkt_set)
        except psycopg.DatabaseError as e:
            print(e, type(e))

        schiffe = {mmsi: schiff
                   for mmsi, schiff in schiffe.items()
                   if 10 <= len(schiff.datenpunkte) <= 500}

    def schiffe(self):
        schiffe = {}
        db_conn: psycopg.Connection
        try:
            with psycopg.connect(**self.config_ais) as db_conn:
                with db_conn.cursor() as cursor:
                    for mmsi, name, typ in cursor.execute('''SELECT mmsi, name, typ
                                                             FROM vessel;''').fetchall():
                        schiffe[mmsi] = Schiff(mmsi, name, typ)

                        for basedatetime, lat, lon in cursor.execute('''SELECT basedatetime, lat, lon
                                                                        FROM vessel
                                                                                 INNER JOIN aisdata on vessel.mmsi = aisdata.mmsi
                                                                        WHERE vessel.mmsi = %s
                                                                        ORDER BY basedatetime;''', (mmsi,)).fetchall():
                            schiffe[mmsi].datenpunkt_hinzufuegen(basedatetime,lat, lon)

        except psycopg.DatabaseError as e:
            print(e, type(e))

        return schiffe


schiffstypen = {0: 'Reserved', 1: 'Reserved', 2: 'Reserved', 3: 'Reserved', 4: 'Reserved', 5: 'Reserved', 6: 'Reserved',
                7: 'Reserved',
                8: 'Reserved', 9: 'Reserved', 10: 'Reserved', 11: 'Reserved', 12: 'Reserved', 13: 'Reserved',
                14: 'Reserved', 15: 'Reserved', 16: 'Reserved', 17: 'Reserved', 18: 'Reserved', 19: 'Reserved',
                20: 'Wing in ground (WIG)', 21: '(WIG), Hazardous cat A', 22: '(WIG), Hazardous cat B',
                23: '(WIG), Hazardous cat C', 24: '(WIG), Hazardous cat D', 25: '(WIG), Reserved',
                26: '(WIG), Reserved', 27: '(WIG), Reserved', 28: '(WIG), Reserved', 29: '(WIG), Reserved',
                30: 'Fishing', 31: 'Towing', 32: 'Towing: length exceeds 200m or breadth exceeds 25m',
                33: 'Dredging or underwater ops', 34: 'Diving ops', 35: 'Military ops', 36: 'Sailing',
                37: 'Pleasure Craft', 38: 'Reserved', 39: 'Reserved', 40: 'High speed craft (HSC)',
                41: '(HSC), Hazardous cat A', 42: '(HSC), Hazardous cat B', 43: '(HSC), Hazardous cat C',
                44: '(HSC), Hazardous cat D', 45: '(HSC), Reserved', 46: '(HSC), Reserved', 47: '(HSC), Reserved',
                48: '(HSC), Reserved', 49: '(HSC), No additional information', 50: 'Pilot Vessel',
                51: 'Search and Rescue vessel', 52: 'Tug', 53: 'Port Tender', 54: 'Anti-pollution equipment',
                55: 'Law Enforcement', 56: 'Spare - Local Vessel', 57: 'Spare - Local Vessel', 58: 'Medical Transport',
                59: 'Noncombatant ship according to RR Resolution No. 18', 60: 'Passenger',
                61: 'Passenger, Hazardous cat A', 62: 'Passenger, Hazardous cat B',
                63: 'Passenger, Hazardous cat C', 64: 'Passenger, Hazardous cat D', 65: 'Passenger, Reserved',
                66: 'Passenger, Reserved', 67: 'Passenger, Reserved', 68: 'Passenger, Reserved',
                69: 'Passenger, No additional information', 70: 'Cargo', 71: 'Cargo, Hazardous cat A',
                72: 'Cargo, Hazardous cat B', 73: 'Cargo, Hazardous cat C', 74: 'Cargo, Hazardous cat D',
                75: 'Cargo, Reserved', 76: 'Cargo, Reserved', 77: 'Cargo, Reserved', 78: 'Cargo, Reserved',
                79: 'Cargo, No additional information', 80: 'Tanker', 81: 'Tanker, Hazardous cat A',
                82: 'Tanker, Hazardous cat B', 83: 'Tanker, Hazardous cat C',
                84: 'Tanker, Hazardous cat D', 85: 'Tanker, Reserved', 86: 'Tanker, Reserved',
                87: 'Tanker, Reserved', 88: 'Tanker, Reserved', 89: 'Tanker, No additional information', 90: 'Other',
                91: 'Other, Hazardous cat A', 92: 'Other, Hazardous cat B', 93: 'Other, Hazardous cat C',
                94: 'Other, Hazardous cat D', 95: 'Other, Reserved', 96: 'Other, Reserved',
                97: 'Other Type, Reserved', 98: 'Other, Reserved', 99: 'Other, no additional information}'}


if __name__ == '__main__':
    dateiname_daten = "AIS_2024_05_29_newyork.csv"

    ais_db = Datenbank('password', setup=True)
    schiffe = ais_db.csv_einlesen(dateiname_daten)