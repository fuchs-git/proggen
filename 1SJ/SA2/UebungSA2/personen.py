from random import randint

personenliste = [
    ("Max Mustermann", ("Kochen", "Tanzen"), ("Rocket League", "Among Us", "Fortnite", "Stardew Valley", "Overwatch")),
    ("Anna Beispiel", ("Malen", "Yoga"), ("The Sims", "Overwatch", "Fall Guys", "Minecraft", "League of Legends")),
    ("Peter Lustig", ("Angeln", "Gartenarbeit"),
     ("Farming Simulator", "Stardew Valley", "Chess", "GTA V", "World of Warcraft")),
    ("Lara Lachen", ("Bungee-Jumping", "Rätsel lösen"),
     ("Portal", "The Witness", "Fall Guys", "Rocket League", "Dota 2")),
    ("Tom Quassel", ("Comedy-Club besuchen", "Kartenspiele"),
     ("Cards Against Humanity", "Uno", "Fortnite", "Overwatch", "Rocket League")),
    ("Emily Spaß", ("Brettspiele", "Fotografie"), ("Catan", "Snapchat", "Minecraft", "The Sims", "Fall Guys")),
    ("Frank Frohsinn", ("Karaoke", "Puzzle lösen"),
     ("SingStar", "Jigsaw Puzzle", "Overwatch", "Fortnite", "Rocket League")),
    ("Lisa Lässig", ("Reisen", "Skateboarden"),
     ("GTA V", "Tony Hawk's Pro Skater", "Fall Guys", "Overwatch", "Minecraft")),
    ("Oliver Optimist", ("Klettern", "Theater spielen"),
     ("Assassin's Creed", "Drama-Adventure-Spiele", "Fall Guys", "Rocket League", "Overwatch")),
    ("Sandra Sonnenschein", ("Stricken", "Bücher lesen"),
     ("World of Warcraft", "The Elder Scrolls V: Skyrim", "Fall Guys", "GTA V", "Minecraft"))]


# Erstellen Sie eine Klasse ZockerFreund,
# die den Namen, die Hobbies (als Tupel) und die Lieblingsspiele (als Tupel)
# eines Zockers kennt.

# Zudem kennt die Klasse das aktuell gezockte Spiel,
# das ist anfangs das erste der Spiele vom Tupel.
# Die Klasse kann sich selbst darstellen mit Name und dem aktuellen gezockten Spiel,
# z.B.: "Max Mustermann zockt Among Us".

class ZockerFreund:
    "Meine Klasse ZockerFreunde"

    def __init__(self, name, hobbies, spiele):
        self.name = name
        self.hobbies = hobbies
        self.spiele = spiele
        self.ls = 0
        self.aktGame = self.spiele[self.ls]

    def __repr__(self):
        return f'{self.name} spielt {self.spiele[self.ls]}'

    def zocken(self):
        if self.ls == len(self.spiele) -1:
            self.ls = 0
        else:
            self.ls += 1
        self.aktGame = self.spiele[self.ls]
        # print(self.__repr__())



a = ZockerFreund("Sandra Sonnenschein", ("Stricken", "Bücher lesen"),
     ("World of Warcraft", "The Elder Scrolls V: Skyrim", "Fall Guys", "GTA V", "Minecraft"))

personen = [ ZockerFreund(*x) for x in personenliste]

# ZockerFreunde können zocken, wodurch diese Ihr Liblingsspiel eine Weile spielen
# (das müssen Sie nicht abbilden) und danach ihr Lieblingsspiel wechseln
# (das nächste Spiel aus dem Tupel, nach dem letzten Spiel wieder das erste)
print(a)
a.zocken()

# erstellen Sie aus den Daten "personenliste" eine Liste Ihrer Zockerfreunde
# Geben Sie den Inhalt der Liste (untereinander) aus.

#print(*personen, sep='\n')

# Lassen Sie jeden Ihrer ZockerFreunde zufällig 50 bis 200 Mal jeweils zocken.

for p in personen:
    for _ in range(randint(50,200)):
        p.zocken()

# Gibt es ZockerFreunde, die jetzt zufällig das gleiche Spiel spielen?
# Geben Sie diese Freunde aus unter Nennung, des Spiels aus.



doppelt = []
liste = []
for p in personen:
    if p.aktGame not in liste:
        liste.append(p.aktGame)
    else:
        doppelt.append(p.aktGame)
print(*personen, sep='\n')
print()
for p in personen:
    if p.aktGame in doppelt:
        print(f'{p.name} spielt {p.aktGame}')

