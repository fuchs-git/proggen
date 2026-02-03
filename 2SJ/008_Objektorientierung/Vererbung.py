class Tier:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def sprich(self):
        return 'Tier'

class Katze(Tier):
    def sprich(self):
        return 'miau'

class Hund(Tier):
    def sprich(self):
        return 'wau'

class Wachhund(Hund):
    def sprich(self):
        return super().sprich().upper()

k = Katze("Minka")
h = Hund("Minka")
w = Wachhund("RUDOLF")
print(k)
print(k.sprich())
print(h, h.sprich())
print(w, w.sprich())