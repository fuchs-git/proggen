import functools, time

class UngeradeZahlError(ValueError):
    def __init__(self, zahl, *message):
        ValueError.__init__(self, *message) # Funktionalität der Elternklasse bewahren
        self.zahl = zahl                    # zusätzliches Attribut in der Kind-Klasse

def mach_was(x):
    if x % 2 == 1:
        raise UngeradeZahlError(x, "ungerade Zahl übergeben")
    print(x)


try:
    mach_was(3)
except UngeradeZahlError as e:
    print("das war ein UngeradeZahlError")
    print(f"{e}: {e.zahl}")

# nicht auffangen
mach_was(23)