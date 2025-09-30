import math

hr = "+-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+\n"


# +-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-+
# |P|u|n|k|t|e|.|:|;|!|
# a.    Erstellen Sie, zunächst ohne weiteren Inhalt, eine Klasse Punkt mit einem kurzen Doc-String als Beschreibung!
#
# b.    Erzeugen Sie zwei Objekte p1 und p2 aus Ihrer Klasse!
#       Lassen Sie ihre Objekte mit print ausgeben!
#
# c.    Überschreiben Sie die __init__-Methode Ihrer Klasse! Die Methode soll zwei Parameter bekommen (jeweils als float),
#       mit der die x- und die y-Koordinate des Punktes angegeben werden können. Die übergebenen Parameter sollen als
#       Attribute mit den Namen x und y gespeichert werden. Ergänzen Sie die Erzeugung Ihrer Objekte entsprechend!
#
# d.    Überschreiben Sie die __str__-Methode Ihrer Klasse! Die Ausgabe der Methode soll den Klassennamen gefolgt von den
#       Punktkoordinaten ausgeben. Dabei soll der Klassenname NICHT hard-coded im Code von __str__ stehen!
# +-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-++-+-+-+-+-+-+-+ +-+

class Punkt:
    "Erstellen Sie, zunächst ohne weiteren Inhalt, eine Klasse Punkt mit einem kurzen Doc-String als Beschreibung!"

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def __str__(self):
        return f'Punkt({self.x}|{self.y})'

    def abstand_vom_ursprung(self):
        return math.sqrt((self.x)**2 + (self.y)**2)

    def abstand_von_punkt(self,p2):
        # p2x, p2y = str(punkt).split("(")[1][:-1].split("|")
        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)


p1 = Punkt(4.4,3.3)
p2 = Punkt(4.2,4.9)

print(f'{hr}b) Lassen Sie ihre Objekte mit print ausgeben!\n\t{p1=}\n\t{p2=}')
print(p1, p2)
print(f'{hr}e) Erzeugen Sie in der Klasse eine Methode abstand_vom_ursprung, welche den Abstand eines Punkts vom '
      f'Koordinaten-Ursprung bei (0|0) zurückgibt.\n {p1.abstand_vom_ursprung()}')

p1 = Punkt(6.5, 4.5)
p2 = Punkt(3.2, 0.1)
print(f'{hr} f) Erzeugen Sie in der Klasse eine Methode abstand_von_punkt, welche einen (anderen) Punkt übergeben'
      f' bekommt und den Abstand des eigenen Punktes zum übergebenen Punk zurückgibt.')
print(p1)
print(p2)
print(p1.abstand_von_punkt(p2))
print(p2.abstand_von_punkt(p1))
print(p1.abstand_von_punkt(p1))
print(type(p1).__name__)
print(p1.__sizeof__())
