import math


def pythagoras(p1x:float, p1y:float, p2x:float, p2y:float) -> float:
    """
    Das ist eine Übungsaufgabe für tolle Mathe Funktionen in python. Python ist toll, Mathe ist !toll.
    :param p1x: Hier wird der X-Achsenwert für den Punkt 1 angegeben.
    :param p1y: Hier wird der Y-Achsenwert für den Punkt 1 angegeben.
    :param p2x: Hier wird der X-Achsenwert für den Punkt 2 angegeben.
    :param p2y: Hier wird der Y-Achsenwert für den Punkt 2 angegeben.
    :return: Es wird ein float zurückgegeben
    """
    a= p2y - p1y
    b= p2x - p1x
    c = (a*a + b*b)
    return math.sqrt(c)

print(pythagoras(2,2,3,3))