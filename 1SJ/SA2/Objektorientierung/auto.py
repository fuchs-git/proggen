from random import randint


class Auto:
    """
    eine Klasse für Autos
    """

    def __init__(self, marke: str, modell: str, baujahr: int):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.kilometerstand = 0  # Attribut ohne Parametereinfluss

    def __str__(self) -> str:
        return f"{self.marke} {self.modell} (BJ {self.baujahr})"

    def fahre(self, kilometer: int):
        print(f'{self.__str__()} fährt {kilometer}km.')
        self.kilometerstand += kilometer


auto_daten = [('Toyota', 'Corolla', 1984),
              ('Tesla', 'Model 3', 2022),
              ('Opel', 'Manta', 1989)]
auto_liste = [Auto(*details) for details in auto_daten]  # mehrere Autos aus einer Datenquelle
auto_liste.append(Auto('BMW', '3er Kombi', 2007))  # ein einzelnes Auto

print(*auto_liste)
exit()

print('Neuwagen:')
for auto in auto_liste:
    print(auto, 'mit', auto.kilometerstand, 'Kilometern')

print()
print()

for _ in range(20):
    wer = randint(1, len(auto_liste)) - 1
    wieweit = randint(10, 100)
    auto_liste[wer].fahre(wieweit)

print()
print()

print('Gebrauchtwagen:')
for auto in auto_liste:
    print(auto, 'mit', auto.kilometerstand, 'Kilometern')