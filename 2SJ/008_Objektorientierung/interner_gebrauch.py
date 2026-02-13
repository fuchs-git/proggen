class Katze:
    def __init__(self, name):
        self.name = name            # Attribut ohne Unterstrich => soll jeder Nutzer der Klasse benutzen
        self._stimmung = "mies"     # Attribut mit Unterstrich => soll nur Klassen-intern benutzt werden

    def sprich(self):
        if self._stimmung == "mies":
            return "fauchen"
        else:
            return "miau"

k = Katze("Minka")

print(k.name)  # das geht
print(k.sprich())  # das geht
print(k._stimmung) # das geht, SOLL MAN ABER NICHT MACHEN