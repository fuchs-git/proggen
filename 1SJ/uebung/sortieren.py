from random import randint


class RGBFarbe:
    def __init__(self, r: int, g: int, b: int):
        self.r = self.check(r)
        self.g = self.check(g)
        self.b = self.check(b)
        self.helligkeit = self.r + self.g + self.b

    def check(self, wert):
        return 0 if wert <= 0 else 255 if wert > 255 else wert

    def __repr__(self):
        # return f'Rot:\t{self.r}\nGrün:\t{self.g}\nBlau:\t{self.b}'
        return f'RGB({self.r},{self.g},{self.b})'

    def __eq__(self, other: 'RGBFarbe'):
        # 4. Sorgen Sie dafür, dass zwei verschiedene Objekte mit gleichen Attributen als gleich erkannt werden.
        return self.r == other.r and self.g == other.g and self.b == other.b

    # 8. Machen Sie die Objekte der Klasse sortierbar, indem Sie die Methode __lt__ implementieren (»lt« steht für
    # »less than« und entspricht dem »<« Operator). Die Methode soll genau dann True zurückgeben, wenn die Helligkeit
    # des eigenen Objektes kleiner ist, als die Helligkeit des Vergleichsobjektes (und False sonst).
    def __lt__(self, other:'RGBFarbe'):
        return self.helligkeit < other.helligkeit

    def __hash__(self):
        return hash((self.r, self.g, self.b, self.helligkeit))


# 2. Erzeugen Sie drei Objekte der Klasse RGBFarbe, wobei zwei davon identische Attribute haben, während die Attribute
# des dritten Objekts von den ersten beiden abweichen sollen! Lassen Sie die Objekte mit print ausgeben.
farbe1 = RGBFarbe(-100, 100, 300)
farbe2 = RGBFarbe(-100, 100, 300)
farbe3 = RGBFarbe(23, 150, 42)

# 3. Vergleichen Sie die drei Objekte mit == (jedes mit jedem anderen).
# 5. Vergleichen Sie die drei Objekte mit == (jedes mit jedem anderen).
print(f'{farbe1=} == {farbe2=} = {farbe1 == farbe2}')
print(f'{farbe1=} == {farbe3=} = {farbe1 == farbe3}')
print(f'{farbe2=} == {farbe3=} = {farbe2 == farbe3}')

# 6. Erzeugen Sie eine Liste von 10 Objekten der Klasse RGBFarbe, deren Farbwerte zufällig belegt sind und lassen Sie die Liste ausgeben.
farben = [RGBFarbe(randint(0,255), randint(0,255), randint(0,255)) for i in range(10)]

# 7. Versuchen Sie, die Liste mit der Funktion sorted zu sortieren! Lesen und verstehen Sie die Fehlermeldung.
# print(sorted(farben))

# 9. Geben Sie die eine sortierte Kopie der Liste aus.
print(sorted(farben))

# Erzeugen Sie eine Menge aller bisher angelegten RGBFarbe-Objekte (also sowohl die Einzel-Objekte als auch alle Elemente der Liste).
farben_set = set()
farben_set.update(farben)
farben_set.add(farbe1)
farben_set.add(farbe2)
farben_set.add(farbe3)

print(farben_set)

