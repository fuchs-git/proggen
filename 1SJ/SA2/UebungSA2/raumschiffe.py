raumschiffe = [
    ("USS Enterprise", "Federation", 250, 2000, "Shuttle", "Exploration"),
    ("Millennium Falcon", "Rebel Alliance", 350, 800, "Transport", "Smuggling"),
    ("Star Destroyer", "Empire", 500, 1500, "Capital Ship", "Conquest"),
    ("Serenity", "Independents", 180, 500, "Cargo", "Transport"),
    ("Battleship Galactica", "Colonial Fleet", 450, 2200, "Battleship", "Defense"),
    ("Discovery One", "NASA", 100, 3000, "Exploration", "Research"),
    ("TIE Fighter", "Empire", 50, 300, "Fighter", "Battle"),
    ("X-Wing", "Rebel Alliance", 70, 400, "Fighter", "Battle"),
    ("Enterprise D", "Federation", 300, 2300, "Flagship", "Exploration"),
    ("Viper Mark II", "Colonial Fleet", 60, 600, "Fighter", "Battle"),
    ("Nostromo", "Commercial", 120, 500, "Cargo", "Transport"),
    ("Borg Cube", "Borg Collective", 1000, 5000, "Capital Ship", "Assimilation"),
    ("Discovery Two", "NASA", 110, 3500, "Exploration", "Research"),
    ("Defiant", "Federation", 250, 1600, "Destroyer", "Defense"),
    ("Leviathan", "Rebel Alliance", 400, 1200, "Battleship", "Conquest"),
    ("Romulan Warbird", "Romulan Empire", 450, 1400, "Capital Ship", "Infiltration"),
    ("Aurora", "Private", 60, 800, "Exploration", "Research"),
    ("Phoenix", "Federation", 200, 1500, "Explorer", "Exploration"),
    ("Blackbird", "X-Men", 150, 600, "Shuttle", "Reconnaissance"),
    ("Nemesis", "Borg Collective", 1100, 6000, "Capital Ship", "Assimilation")
]


class Raumschiff():
    def __init__(self, name: str, fraktion: str, mannschaftskapazitaet: int, reichweite: int, schiffstyp: str,
                 mission: str):
        self.name = name
        self.fraktion = fraktion
        self.kapazitaet = mannschaftskapazitaet
        self.reichweite = reichweite
        self.schiffstyp = schiffstyp
        self.mission = mission

    def __repr__(self):
        return f"Raumschiff: {self.name}\nFraktion: {self.fraktion}\nMannschaftskapazität: {self.kapazitaet}\nReichweite: {self.reichweite} Lichtjahre\nSchiffstyp: {self.schiffstyp}\nMission: {self.mission}"


class RaumschiffFlotte():
    def __init__(self):
        self.flotte = []

    def hinzu(self, schiff: Raumschiff):
        self.flotte.append(schiff)
        # print(f'Folgendes Schiff wurde hinzugefügt:\n{schiff}\n')

    def reichweite(self):
        a = sorted([x for x in self.flotte], key=lambda x: x.reichweite)
        return "\n".join([f'{x.reichweite:_} - {x.name}' for x in a])

    def fraktionen_filter(self, fraktion:str):
        a = sorted([x for x in self.flotte if x.fraktion == fraktion], key=lambda x: x.kapazitaet)
        return "\n".join([f'{x.fraktion} - {x.name}' for x in a])

    def typ_filter(self, typ:str):
        a = sorted([x for x in self.flotte if x.schiffstyp == typ], key=lambda x: x.kapazitaet)
        return "\n".join([f'{x.schiffstyp} - {x.name}' for x in a])

    def reichweite(self):
        return round(sum([x.reichweite for x in self.flotte]) / len(self.flotte))

meineFlotte = RaumschiffFlotte()
schiff = Raumschiff("Voyager", "Federation", 220, 1337, "Discovery", "Exploration")
schiff2 = Raumschiff('Andromeda', 'Federation', 300, 2500, 'Explorer', 'Exploration')
meineFlotte.hinzu(schiff)
meineFlotte.hinzu(schiff2)
schiffe = [Raumschiff(*x) for x in raumschiffe]
[meineFlotte.hinzu(x) for x in schiffe]
# print(meineFlotte.reichweite())
print(meineFlotte.fraktionen_filter('Rebel Alliance'))
print(meineFlotte.typ_filter('Fighter'))
print(meineFlotte.reichweite())
