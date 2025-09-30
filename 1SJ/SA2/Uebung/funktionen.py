filme = [
    "Casablanca", "Der Pate", "Psycho", "Die Vögel", "Vertigo",
    "Citizen Kane", "Das Fenster zum Hof", "Gone with the Wind",
    "Lawrence von Arabien", "Die zehn Gebote", "Metropolis",
    "King Kong", "Das Apartment", "Sunset Boulevard", "Dr. Strangelove",
    "Das Boot", "West Side Story", "Ben Hur", "Goldrausch", "Die Brücke am Kwai"
]

print(f'{filme[0]} und {filme[-1]}')

filme[1]="Das Leben des Brain"
print(filme)

for elem in filme:
    if elem[0].lower()<= 'm':
        print(elem, end=' ')
print()

filme_zehn = []
[filme_zehn.append(elem) for elem in filme if len(elem) >= 10]
print(filme_zehn)
filme_zehn.sort()

for elem in filme_zehn:
    print(f'{filme_zehn.index(elem)+1:3}. {elem}')

