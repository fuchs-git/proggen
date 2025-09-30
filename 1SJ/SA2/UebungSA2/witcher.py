witcher_characters_dataset = [
    ("Geralt von Riva", ("Stahlschwert", "Silberschwert", "Magie"), "Königreich: Kein dauerhaftes Königreich, wandernder Hexer", "Hexer, Schwertkämpfer, Magier", 100),
    ("Yennefer von Vengerberg", ("Magie",), "Königreich: Kein Königreich, Magierin aus Vengerberg", "Magierin, Beschützerin, Liebhaberin von Geralt", 95),
    ("Triss Merigold", ("Magie",), "Königreich: Redania", "Magierin, Heilerin, Freundin von Geralt", 90),
    ("Ciri (Cirilla Fiona Elen Riannon)", ("Stahlschwert", "Silberschwert", "Magie"), "Königreich: Cintra", "Prinzessin, Kriegerin, Trägerin des ‘Elder Blood’", 98),
    ("Ritterspon", ("Lute",), "Königreich: Redania", "Barde, Poet, Freund von Geralt", 50),
    ("Vesemir", ("Stahlschwert",), "Königreich: Kein dauerhaftes Königreich, ältester Hexer von Kaer Morhen", "Hexer, Lehrer, Vaterfigur", 85),
    ("Zoltan Chivay", ("Axt",), "Königreich: Mahakam (Zwergenheimat)", "Zwerg, Krieger, Freund von Geralt", 75),
    ("Lambert", ("Stahlschwert",), "Königreich: Kein dauerhaftes Königreich, Hexer von Kaer Morhen", "Hexer, Krieger, ungehobelt", 80),
    ("Eskel", ("Stahlschwert",), "Königreich: Kein dauerhaftes Königreich, Hexer von Kaer Morhen", "Hexer, Krieger, Friedlicher", 82),
    ("Shani", ("Keine",), "Königreich: Temeria", "Ärztin, Heilerin, Freundin von Geralt", 65),
    ("Emhyr var Emreis", ("Keine",), "Königreich: Nilfgaard", "Herrscher, Politiker, manipulierend", 99),
    ("Regis", ("Keine",), "Königreich: Kein Königreich, Vampir aus der Region der Hexer", "Vampir, Heiler, Freund von Geralt", 92),
    ("Cahir Mawr Dyffryn aep Ceallach", ("Stahlschwert",), "Königreich: Nilfgaard", "Ritter, Kämpfer, loyal", 88),
    ("Philippa Eilhart", ("Magie",), "Königreich: Redania", "Magierin, Politikerin, Intrigantin", 94),
    ("Iorveth", ("Bogen", "Dolch"), "Königreich: Scoia'tael (Nichtmenschengruppen)", "Elfenkrieger, Anführer, Freiheitskämpfer", 87),
    ("Sirius von Vengerberg", ("Keine",), "Königreich: Vengerberg", "Magier, Mentor, Opfer der Umstände", 70),
    ("Tissaia de Vries", ("Magie",), "Königreich: Aretusa (Akademie der Magier)", "Magierin, Lehrerin, Autoritätsperson", 93)
]


class Held:
    def __init__(self, name, waffen, koenigreich, eigenschaften,level):
        self.name = name
        self.waffen = waffen
        self.koenigreich = koenigreich
        self.eigenschaften = eigenschaften
        self.level = level

    def __repr__(self):
        return f'{self.name} - {self.level} - {self.eigenschaften} - {self.waffen}'


class Arena:
    def __init__(self, name):
        self.name = name
        self.helden = []

    def __repr__(self):
        return ' '.join([h for h in self.helden])

    def hinzu(self):
        pass

    def kaempfen(self):
        pass




# Klasse: Held
#
# Die Klasse Held soll folgende Attribute besitzen:
# name: Der Name des Helden.
# waffen: die Waffen des Helden
# koenigreich: das Königreich des Helden
# eigenschaften des Helden.
# level: Das Level des Helden.

# Helden werden mit: name - lvl - eigenschaft - waffen dargestellt.
#
# Klasse: Arena
#
# Die Klasse Arena soll folgende Attribute besitzen:
# name (String): Der Name der Arena.
# helden (Liste): Eine Liste der Helden, die in der Arena kämpfen können.
# Die Klasse kann:
#                   Helden hinzufuegen.
#                   Helden kaempfen lassen.
#                               Dabei gilt : Lässt zwei Helden gegeneinander kämpfen.
#                               Der Sieger wird durch die Formel bestimmt: held1 = level + random.randint(1, 20) vs held2 = level + random.randint(1, 20) .
#                               Der Held mit dem höheren Wert gewinnt.
#                               Gibt den Namen des Gewinners aus.
#                               Falls beide gleich stark sind, soll ein Unentschieden ausgegeben werden.
#
# Die Klasse Arena stellt sich wie folgt dar: Gibt alle Helden in der Arena aus.
#
# Erstelle eine Arena mit einem beliebigen Namen.
# Erstelle alle Helden gem. witcher_characters_dataset.
# Füge die Helden der Arena hinzu.
# Lass mindestens zwei Kämpfe zwischen 2 Helden stattfinden.
# Gib die Ergebnisse der Kämpfe aus.


# Output könnte dabei so aussehen:
## Arena: Kampfarena
## Held hinzugefügt: Geralt (Level 100)
## Held hinzugefügt: Ciri (Level 98)
## Held hinzugefügt: Yennefer (Level 95)
## Held hinzugefügt: Lambert (Level 80)
#
## Helden in der Arena:
## - Geralt (Level 100)
## - Ciri (Level 98)
## - Yennefer (Level 95)
## - Lambert (Level 80)
#
## Kampf: Geralt vs Ciri
## Geralt gewinnt mit einem Wert von 112 gegen Ciri mit einem Wert von 105!
#
## Kampf: Yennefer vs Lambert
## Lambert gewinnt mit einem Wert von 85 gegen Yennefer mit einem Wert von 82!

print(f"{0x1F40D:c}")
print(u'\u1280')
print(0x1f40d)