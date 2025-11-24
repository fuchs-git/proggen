import math
from datetime import datetime
import datenbank as db


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
                    self.datenpunkte.add((datetime.strptime(zeit, "%Y-%m-%dT%H:%M:%S"), float(lat), float(lon)))


        except FileNotFoundError:
            print(f"Datei {self.dateiname} nicht gefunden")
        except OSError:
            print(f"Fehler beim Lesen der Datei {self.dateiname}")




csv = CSV("AIS_2024_05_29_newyork.csv")
ais_db = db.Datenbank('password')
ais_db.erstelle_db()
ais_db.befuellen(csv.schiffe, csv.datenpunkte)