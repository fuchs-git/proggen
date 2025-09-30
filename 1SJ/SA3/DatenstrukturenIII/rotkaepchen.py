# 1-2 Schreiben Sie ein Python-Programm, welches die Datei im Textmodus öffnet und einliest! Dabei soll die erste Zeile der
# Datei ignoriert/weggelassen werden, der restliche Dateiinhalt soll in den String inhalt eingelesen werden
# (inklusive aller Zeilenumbrüche).

# with open('Rotkäppchen.txt', 'r') as f:
#     f.readline()
# # 3 Ersetzen Sie im String inhalt alle Großbuchstaben durch ihren jeweiligen Kleinbuchstaben.
#     inhalt = f.read().lower()

# Ersetzen Sie im String inhalt alle Zeichen, die kein Buchstabe sind, durch ein Leerzeichen! Beachten Sie dabei, dass
# es in unserer Sprache 30 Buchstaben gibt (und eventuell noch Buchstaben, die Varianten von anderen Buchstaben sind, wie »é«).

# meineBuchstaben = 'qwertzuiopüasdfghjklöäyxcvbnméèáàß'
# for b in inhalt:
#     if not b in meineBuchstaben:
#         inhalt = inhalt.replace(b,' ')

# inhalt = ''.join([ x if x in meineBuchstaben else ' ' for x in inhalt])
# inhalt = ' '.join(inhalt.split())


# Erzeugen Sie aus dem String inhalt ein Dictionary, welches die Vorkommen der einzelnen Worte zählt. Dafür zerlegen Sie
# den String anhand seiner Leerzeichen in Worte und iterieren über das Ergebnis und prüfen für jedes Wort, ob es schon im
# Dictionary vorhanden ist. Wenn nein, wird das Wort als neuer Schlüssel mit dem Wert 1 zum Dictionary hinzugefügt.
# Wenn ja, wird der Wert des Schlüssels um eins erhöht.

# worte = inhalt.split()
# wort_dict = {}
# for wort in worte:
#     if wort in wort_dict:
#         wort_dict[wort] += 1
#     else:
#         wort_dict[wort] = 1
#
# print(wort_dict)
# print(max(wort_dict,key=wort_dict.get))
# print(max(wort_dict.values()))


# Nutzen Sie das gleiche Programm, um die Worte in dieser Datei zu zählen und das häufigste Wort zu ermitteln (hier sollte das häufigste Wort 5.060-mal auftreten).
# Nutzen Sie das gleiche Programm, um die Worte in dieser Datei zu zählen und das häufigste Wort zu ermitteln (hier sollte das häufigste Wort 46.333-mal auftreten).

def wort_zaehler(dateiname):
    meineBuchstaben = 'qwertzuiopüasdfghjklöäyxcvbnméèáàß'
    with open(dateiname, 'r') as f:
        f.readline()
        inhalt = f.read().lower()
    inhalt = ''.join([x if x in meineBuchstaben else ' ' for x in inhalt])
    inhalt = ' '.join(inhalt.split())
    worte = inhalt.split()
    wort_dict = {}
    for wort in worte:
        if wort in wort_dict:
            wort_dict[wort] += 1
        else:
            wort_dict[wort] = 1
    return max(wort_dict,key=wort_dict.get), max(wort_dict.values())


    # a = sorted(wort_dict, key=lambda x: wort_dict[x])
    # a, b = sorted(wort_dict.items(), key=lambda x: x[1])[-1]
    # return (a, b)


print(wort_zaehler('Rotkäppchen.txt'))
print(wort_zaehler('Memoiren_einer_Sozialistin.txt'))
print(wort_zaehler('Bibel.txt'))
