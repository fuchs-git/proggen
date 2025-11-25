import math
import psycopg
from datetime import datetime


from schiffstypen import schiffstypen


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

    def __eq__(self, other:"Schiff"):
        return self.mmsi == other.mmsi

    def __hash__(self):
        return hash(self.mmsi)

    def datenpunkt_hinzufuegen(self, zeit: datetime, lat:float, lon:float):

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


class CSV:
    def __init__(self, dateiname: str):
        self.dateiname = dateiname
        self.schiffe = set()
        self.datenpunkte = set()
        self._datei_lesen()

    def _datei_lesen(self):
        schiffe = {}
        try:
            with open(self.dateiname) as file:
                print(file.readline())  # erste Zeile weglassen (Header)

                for zeile in file:

                    # MM, Time, LAT, LON, S, C, H, Name, I, C, Typ, S, Length, Width,Draft,Cargo,TransceiverClass
                    mmsi, zeit, lat, lon, _, _, _, name, _, _, typ, *_ = zeile.split(",")

                    # Dict Möglichkeit
                    # if mmsi not in vessel:
                    #     vessel[mmsi] = Schiff(mmsi,name,int(typ) if typ else 99)
                    #
                    # vessel[mmsi].datenpunkt_hinzufuegen(datetime.strptime(zeit, "%Y-%m-%dT%H:%M:%S"), float(lat), float(lon))

                    self.schiffe.add((mmsi,name,int(typ) if typ else 99))
                    self.datenpunkte.add((mmsi, datetime.strptime(zeit, "%Y-%m-%dT%H:%M:%S"), float(lat), float(lon)))


        except FileNotFoundError:
            print(f"Datei {self.dateiname} nicht gefunden")
        except OSError:
            print(f"Fehler beim Lesen der Datei {self.dateiname}")

class Datenbank:
    def __init__(self, password: str, install: bool = False):
        self.config_setup = {'user': 'postgres',
                             'password': password,
                             'dbname': 'postgres',
                             'host': 'localhost',
                             'port': 5432,
                             'autocommit': True}
        self.config_ais = {'user': 'postgres',
                           'password': password,
                           'dbname': 'ais',
                           'host': 'localhost',
                           'port': 5432,
                           'autocommit': True}

        if install:
            self.erstelle_db()

    def erstelle_db(self):

        try:
            db_conn: psycopg.Connection
            with psycopg.connect(**self.config_setup) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute('DROP DATABASE IF EXISTS ais')
                    cursor.execute('CREATE DATABASE ais')
        except psycopg.DatabaseError as e:
            print(e, type(e))

        try:
            db_conn: psycopg.Connection
            with psycopg.connect(**self.config_ais) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.execute("""
                                   CREATE TABLE vessel (
                                       mmsi INT PRIMARY KEY,
                                       name TEXT,
                                       typ  TEXT
                                   )
                                   """)

                    cursor.execute("""
                                   CREATE TABLE aisdata (
                                       mmsi         INT REFERENCES vessel (mmsi),
                                       basedatetime TIMESTAMP,
                                       lat          DECIMAL,
                                       lon          DECIMAL,
                                       PRIMARY KEY (mmsi, basedatetime)
                                   )""")
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def befuellen(self, schiffe, koordinaten):
        try:
            with psycopg.connect(**self.config_ais) as db_conn:
                with db_conn.cursor() as cursor:
                    cursor.executemany('''INSERT INTO vessel (mmsi, name, typ)
                                          VALUES (%s, %s, %s)''', schiffe)
                    cursor.executemany('''INSERT INTO aisdata (mmsi, basedatetime, lat, lon) VALUES (%s, %s, %s, %s)''', koordinaten)
        except psycopg.DatabaseError as e:
            print(e, type(e))

    def schiffe(self):
        try:
            with psycopg.connect(**self.config_ais) as db_conn:
                with db_conn.cursor() as cursor:
                    schiffe = {}
                    for mmsi, name, typ in cursor.execute(
                            '''SELECT mmsi, name, typ
                               FROM vessel'''
                    ).fetchall():
                        schiffe[mmsi] = Schiff(mmsi, name, typ)

                    for mmsi, schiff in schiffe.items():
                        for zeit, lat, lon in cursor.execute(
                                """SELECT basedatetime, lat, lon
                                   FROM vessel
                                            INNER JOIN aisdata ON vessel.mmsi = aisdata.mmsi
                                   WHERE vessel.mmsi = %s
                                   ORDER BY basedatetime;""",
                                (mmsi,)
                        ).fetchall():
                            schiff.datenpunkt_hinzufuegen(zeit, lat, lon)

                    return schiffe  # ← WICHTIG!
        except psycopg.DatabaseError as e:
            print(e, type(e))


if __name__ == '__main__':
    #db = Datenbank('password', install=True)


    csv = CSV("AIS_2024_05_29_newyork.csv")
    ais_db = Datenbank('password')
    ais_db.befuellen(csv.schiffe, csv.datenpunkte)