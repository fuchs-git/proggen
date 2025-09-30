linien_daten = [
    (760, ('Berlin, Alexanderplatz', 'Berlin, Kurfürstendamm', 'Potsdam, Sanssouci')),
    (761, ('Hamburg, Jungfernstieg', 'Hamburg, Reeperbahn',
     'Lübeck, Holstentor', 'Lübeck, Hauptbahnhof')),
    (762, ('München, Marienplatz', 'München, Odeonsplatz',
     'Augsburg, Rathausplatz', 'Augsburg, Hauptbahnhof', 'München, Hauptbahnhof')),
    (763, ('Frankfurt, Hauptwache', 'Frankfurt, Konstablerwache', 'Mainz, Hauptbahnhof',
     'Wiesbaden, Kurhaus', 'Frankfurt, Flughafen', 'Frankfurt, Römer')),
    (764, ('Köln, Dom/Hbf', 'Bonn, Beethovenhaus', 'Köln, Messe/Deutz')),
    (765, ('Dresden, Zwinger', 'Leipzig, Hauptbahnhof',
     'Dresden, Hauptbahnhof', 'Leipzig, Völkerschlachtdenkmal')),
    (766, ('Stuttgart, Hauptbahnhof', 'Karlsruhe, Europaplatz', 'Stuttgart, Schlossplatz',
     'Karlsruhe, Hauptbahnhof', 'Stuttgart, Vaihingen', 'Stuttgart, Zuffenhausen', 'Stuttgart, Feuerbach')),
    (767, ('Düsseldorf, Altstadt', 'Essen, Hauptbahnhof', 'Duisburg, Landschaftspark')),
    (768, ('Bremen, Marktplatz', 'Hannover, Kröpcke', 'Bremen, Hauptbahnhof')),
    (769, ('Nürnberg, Hauptmarkt', 'Erlangen, Arcaden',
     'Fürth, Rathaus', 'Nürnberg, Flughafen', 'Nürnberg, Messe')),
    (770, ('Aachen, Elisenbrunnen', 'Mönchengladbach, Hauptbahnhof', 'Aachen, RWTH Aachen Campus', 'Mönchengladbach, Alter Markt',
     'Aachen, Hauptbahnhof', 'Aachen, Klinikum', 'Aachen, Vaals', 'Aachen, Campus Melaten', 'Aachen, Schanz', 'Aachen, Burtscheid')),
    (771, ('Freiburg, Bertoldsbrunnen', 'Basel, Bahnhof SBB', 'Freiburg, Hauptbahnhof')),
    (772, ('Kiel, Hauptbahnhof', 'Lübeck, Hauptbahnhof', 'Kiel, Holstenstraße',
     'Lübeck, Trave', 'Kiel, Universität', 'Kiel, Schilksee'))
]

liste = sorted(linien_daten, key=lambda x : (x[::-1],len(x)))

#Aufgabe1# Erstellen Sie eine Klasse Linie die eine Buslinie repräsentieren soll.
# Die Klasse Linie kennt ihre Nummer und ihre Stationen und kann diese ausgeben
#Auserdem kann die Klasse Linie die Anzahl ihrer stationen zurückgeben

class Linie:
    """
    Es fährt ein Bus, nach nirgendwo
    """
    def __init__(self, nummer, stationen):
        self.nummer = nummer
        self.stationen = stationen

    def __repr__(self):
        return f'{self.nummer} Fahrplan: {self.stationen}'

#Aufgabe2#Erstellen Sie die Klasse Bus
#Die Klasse Bus kennt die ihr zugewiesene linie
#Die Klasse Bus kennt ihre derzeitige position
#Die Klasse Bus kennt ihre Fahrtrichtung (ob die Linie hin oder zurück gefahren wird = also vorwaerts/rueckwerts)


class Bus:
    def __init__(self, linie:Linie, richtung='vorwärts'):
        self.linie = linie
        self.richtung = richtung
        self.index = 0
        self.position = self.linie.stationen[self.index]


    def __repr__(self):
        return f'{self.linie.nummer} {self.position} Fahrtrichtung: {self.richtung}'

    # Die Klasse Bus kann fahren, jeweils immer eine station weiter. Sollte nach dem fahren eine Endstation erreicht werden,
    # dreht der Bus selbstständig und würde bei der Weiterfahrt die linie weiter befahren.
    # ( von A über B zu C dann drehen und über B zu A und drehen usw..)

    def fahren(self):
        self.index += 1
        if self.index == len(self.linie.stationen)-1:
            print("Endstation, der Bus wendet")
            self.index = 0
            self.linie.stationen = self.linie.stationen[::-1]
            if self.richtung=='vorwärts':
                self.richtung='rückwärts'
            else:
                self.richtung = 'vorwärts'
        self.position = self.linie.stationen[self.index]

    def naechteStation(self):
        return self.linie.stationen[self.index + 1]

linien = [Linie(*x) for x in linien_daten]

bus1 = Bus(linien[0])




#Die klasse Bus kann ihre Linie, die aktuelle Position und Fahrtrichtung als lesbare Zeichenkette ausgeben.
print(bus1.linie)
#Die Klasse Bus kann ihre nächste Station anzeigen lassen
print(bus1)
print(bus1.naechteStation())
bus1.fahren()
print(bus1.naechteStation())
bus1.fahren()
print(bus1.naechteStation())
bus1.fahren()

print(bus1.naechteStation())
bus1.fahren()