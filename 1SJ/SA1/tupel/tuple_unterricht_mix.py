def vorstellen(name, alter, beruf):
    print(f'{name} ist {alter} Jahre alt und von Beruf {beruf}.')


# anlegen
namen = ["Alice", "Bob", "Charlie"]
alter = [35, 42, 27]
berufe = ['Angestellte', 'Beamter', 'Clown']

# unzusammenhängend darstellen
print(namen, alter, berufe)

# gemeinsam ändern  (nie nur eine der Listen ändern)
namen.append('Doris')
alter.append(33)
berufe.append('Dachdecker')

for i in range(len(namen)):     # einen Index bauen, der für alle drei Listen benutzt werden muss
    vorstellen(namen[i], alter[i], berufe[i])


print("".join)

#############################################################################################################

wochentage = ('Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag')
print(wochentage)

test = tuple([x for x in wochentage if "i" in x])
print(test + wochentage)

print(tuple())


def buchstaben_anzahl(text: str):
    for zeichen in text.lower():
        print(zeichen)


print(buchstaben_anzahl('Erdbeereis'))

print(divmod(17, 5))