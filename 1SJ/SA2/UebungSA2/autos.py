vehicles_dataset = [
    ("Tesla Model 3", "Tesla", 2020, "Elektro"),
    ("BMW i3", "BMW", 2018, "Elektro"),
    ("Volkswagen Golf", "Volkswagen", 2015, "Benzin"),
    ("Audi A4", "Audi", 2017, "Diesel"),
    ("Ford Fiesta", "Ford", 2012, "Benzin"),
    ("Mercedes-Benz C-Klasse", "Mercedes-Benz", 2019, "Diesel"),
]


#  Erstelle eine Klasse Fahrzeug, die Name, Hersteller, Baujahr und Antriebsart (z. B. Elektro, Benzin, Diesel) speichert.
#  Erstelle eine Klasse Fahrzeugverwaltung, die folgende Funktionen bietet:
#      Ein Fahrzeug hinzufügen, falls es nicht bereits existiert.
#      Alle Fahrzeuge eines bestimmten Herstellers anzeigen.
#      Die Fahrzeuge nach Baujahr sortieren.
#      Alle Fahrzeuge mit einer bestimmten Antriebsart anzeigen

class Fahrzeug():
    def __init__(self, name: str, hersteller: str, baujahr: int, antrieb: str):
        self.name = name
        self.hersteller = hersteller
        self.baujahr = baujahr
        self.antrieb = antrieb

    def __str__(self):
        return f'{self.name} von {self.hersteller}. Baujahr {self.baujahr} // Antrieb: {self.antrieb}'

    def __repr__(self):
        return f'{self.name};{self.hersteller};{self.baujahr};{self.antrieb}'


class Fahrzeugverwaltung():
    def __init__(self):
        self.flotte = []

    def hinzu(self, kfz: Fahrzeug):
        if kfz not in self.flotte:
            self.flotte.append(kfz)
            print(f'Das Fahrzeug {kfz.name} wurde hinzugefügt')
        else:
            print(f'Das Fahrzeug {kfz.name} befindet sich schon in der Flotte')

    def __str__(self, baujahr=False):
        return "\n".join([str(x) for x in self.flotte])

    def baujahr(self):
        a = sorted([x for x in self.flotte], key=lambda x: x.baujahr)
        return '\n'.join([f'{str(x.baujahr)} {x.name}' for x in a])


sammlung = Fahrzeugverwaltung()
auto = Fahrzeug('911', 'Porsche', 2020, 'Benzin')

sammlung.hinzu(auto)
sammlung.hinzu(auto)

fahrzeuge = [Fahrzeug(*x) for x in vehicles_dataset]
print(fahrzeuge)
[sammlung.hinzu(x) for x in fahrzeuge]
print(sammlung.baujahr())
