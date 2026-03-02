import math

class NegativeWertError(ArithmeticError):
    def __init__(self, zahl, *message):
        ArithmeticError.__init__(self, *message) # Funktionalität der Elternklasse bewahren
        self.zahl = zahl                    # zusätzliches Attribut in der Kind-Klasse

def berechne_wurzel(x):
    if x <0:
        raise NegativeWertError(x, "Der Wert ist kleiner 0.")
    print(math.sqrt(x))



try:
    berechne_wurzel(-10)
except NegativeWertError as e:
    print(f"{e}: {e.zahl}")

# nicht auffangen
berechne_wurzel(10)