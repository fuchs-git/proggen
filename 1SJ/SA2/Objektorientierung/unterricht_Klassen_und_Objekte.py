from time import sleep


class Person:
    """
    eine Klasse für Personen
    """

    def __init__(self, name: str, alter: int):
        print(f'Das Objekt "{name}" wird angelegt, bitte warten....')
        self.name = name
        self.alter = alter
        sleep(2)

    def __str__(self):  # wir überschreiben das eingebaute Verhalten von __str__ mit unserem eigenen
        return f'Ich bin das Objekt {self.name}'

    def __int__(self):
        return self.alter

p1 = Person('Alice', 27)

print(p1)
print(int(p1))

class Gnarf:
    "Das ist meine Klasse"

    def __init__(self, plopp):
        self.plopp = plopp

    def __str__(self):
        return self.plopp *3

    def schnurbzen(self, x):
        return self.plopp / x

g1 = Gnarf(20)
print(g1.schnurbzen(5))