Wuerfel:


def __init__(self):        self.augen = random.randint(1, 6)


def __str__(self):        return str(self.augen)


def werfen(self):        self.augen = random.randint(1, 6)


return self.augenclass
Wuerfelbecher:


def __init__(self):        self.w1 = Wuerfel()


self.w2 = Wuerfel()
self.w3 = Wuerfel()
self.w4 = Wuerfel()
self.w5 = Wuerfel()


def werfen(self):        self.__init__()


def summe(self):        return int(self.w1) + int(self.w2)


def __str__(self):        return f"({self.w1},{self.w2},{self.w3},{self.w4},{self.w5})"


wuerfel = Wuerfelbecher()
print(type(wuerfel.w1))
print(wuerfel)
wuerfel.
import random
from random import randint


class Wuerfel:

    def __init__(self):
        self.augen = random.randint(1, 6)

    def __str__(self):
        return str(self.augen)

    def werfen(self):
        self.augen = random.randint(1, 6)
        return self.augen


class Wuerfelbecher:

    def __init__(self):
        self.w1 = Wuerfel()
        self.w2 = Wuerfel()
        self.w3 = Wuerfel()
        self.w4 = Wuerfel()
        self.w5 = Wuerfel()

    def werfen(self):
        self.__init__()

    def summe(self):
        return int(self.w1) + int(self.w2)

    def __str__(self):
        return f"({self.w1},{self.w2},{self.w3},{self.w4},{self.w5})"


wuerfel = Wuerfelbecher()

print(type(wuerfel.w1))
print(wuerfel)
wuerfel.werfen()
print(wuerfel)
