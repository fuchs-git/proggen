import math
from collections import Counter


def w_to_string(w):
    wochentage = ('Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag')
    return wochentage[w]


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |1|
# Nachschlagen von Werten 1
# Manchmal möchte man ermitteln, welcher Wochentag am 1. Januar eines gegebenen Jahres war/ist/sein wird
# (zumindest möchte das der Programmierlehrer manchmal). Zum Glück gibt es dafür die Gaußsche Wochentagsformel:
#
# w = (1 + 5 * ((A - 1) mod 4) + 4 * ((A - 1) mod 100) + 6 * ((A - 1) mod 400)) mod 7
#
# Dabei ist:
#
# mod: die modulo-Operation (in Python also %)
# A: die vierstellige Jahreszahl
# w: der Wochentag, wobei 0=Sonntag, 1=Montag, ..., 6=Samstag gilt
# Schreiben Sie eine Funktion, die eine vierstellige Jahreszahl übergeben bekommt und den Wochentag des ersten Januars
# dieses Jahres als String zurückliefert!
#
# Hinweis: Die Formel müssen Sie nur richtig abschreiben (kopieren, mod ersetzen, Variablennamen ersetzen).
# Die Umwandlung des Rechenergebnisses w in einen String sollen Sie mit folgendem Tupel erledigen:
#
# wochentage = ('Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag')
# +-+-+-+-+-+-+-+ +-+

def wochentag(jahreszahl):
    w = (1 + 5 * ((jahreszahl - 1) % 4) + 4 * ((jahreszahl - 1) % 100) + 6 * ((jahreszahl - 1) % 400)) % 7
    return w_to_string(w)


print(wochentag(2025))


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |2|
# Nachschlagen von Werten 2
# Hier finden Sie eine Formel für die allgemeine Berechnung des Wochentags zu einem Datum.
#
# Schreiben Sie eine Funktion, die ein Datum als Tag, Monat und Jahr (jeweils Ganzzahlen) übergeben bekommt und
# den Wochentag des Datums als String zurückliefert!
#
# Hinweis: Der gegebene Code ist zwar nicht in Python geschrieben (sondern für LabVIEW), aber Sie werden die wenigen
# notwendigen Änderungen hinbekommen. Die Formel benutzt die Variablen y, m und d für Jahr, Monat und Tag.
# Darüber hinaus benutzt die Formel eine Funktion "floor", welche ganzzahliges Abrunden durchführen soll.
# In Python geht das z.B. mit der int-Funktion.
# +-+-+-+-+-+-+-+ +-+

def wochentagII(y, m, d):
    if (m < 3):
        y = y - 1
    w = ((d + int(2.6 * ((m + 9) % 12 + 1) - 0.2) + y % 100 + int(y % 100 / 4) + int(y / 400) - 2 * int(
        y / 100) - 1) % 7 + 7) % 7 + 1
    return w_to_string(w)


print(wochentagII(2025, 1, 1))


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |3|
# Nachschlagen von Werten 3
# Schreiben Sie eine Funktion, die ein Datum als Tag, Monat und Jahr (jeweils Ganzzahlen) übergeben bekommt und
# ein schön formatiertes Datum als String zurückliefert!
#
# "Schön" soll dabei folgendes bedeuten:
# Wenn Ihre Funktion mit 8, 11 und 2023 als Parameter aufgerufen wird, soll sie "Mittwoch der 8. November 2023" zurückliefern.
# +-+-+-+-+-+-+-+ +-+

def wochentagIII(y, m, d):
    months = 'Januar Februar März April Mai Juni Juli August September Oktober November Dezember'.split()
    return f'{wochentagII(y, m, d)} der {d}. {months[m - 1]} {y}'


print(wochentagIII(2023, 11, 8))


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |4|
# Mehrfache Rückgabe 1
# Schreiben Sie eine Funktion division_ganzzahlig, die zwei (ganze) Zahlen übergeben bekommt und die daraus zwei Werte
# berechnet und zurückliefert - das Ergebnis der ganzzahligen Division UND den Rest der ganzzahligen Division!
# Ihre Funktion soll sinnvoll auf fehlerhafte Parameter reagieren (falscher Typ, Division durch 0, ...)
#
# Hinweis 1: Funktionen können nur einen Wert (oder ein Ding) zurückliefern (oder gar keinen, aber nie mehr als einen).
# Um nun doch mehrere Werte zurückliefern zu können, packt man diese in ein Tupel und liefert das Tupel zurück (das ist ja genau ein Ding).
# +-+-+-+-+-+-+-+ +-+

def division_ganzzahlig(a, b):
    return divmod(a, b)

print(division_ganzzahlig(8, 5))


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |5|
# Pythagoras
# Schreiben Sie eine Funktion pythagoras, die zu zwei gegebenen Punkten P1 und P2, jeweils mit deren x- und y-Werten,
# den Abstand dazwischen berechnet. Die Funktion bekommt ZWEI Parameter übergeben - für jeden der Punkte ein Tupel.
# Jedes der Tupel besteht aus einer x-Koordinate und einer y-Koordinate.
# +-+-+-+-+-+-+-+ +-+

def pythagoras(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    distance = math.sqrt(dx ** 2 + dy ** 2)
    return distance


p1 = (1, 1)
p2 = (5, 4)
print(pythagoras(p1, p2))


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |6|
# Schreiben Sie eine Funktion int_filter, die eine Liste übergeben bekommt. Die Funktion soll ZWEI Listen zurückgeben.
# Die erste Liste soll alle ganzen Zahlen (also alle int-Werte) der Eingabeliste enthalten, die zweite Liste soll alle
# anderen Elemente der Eingabeliste enthalten.
# +-+-+-+-+-+-+-+ +-+

def int_filter(a):
    zahlen = [elem for elem in a if type(elem) == int]
    keineZahl = [elem for elem in a if not type(elem) == int]
    return zahlen, keineZahl


gemischteListe = [11, 1, "a", 5, True, 3.4, 2]
print(int_filter(gemischteListe))

# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |7|
# Mehrfache Rückgabe 3
# Erstellen Sie eine Liste, bestehend aus mindestens zehn unterschiedlichen aber gleichförmigen Tupeln
# (also Tupeln, die die gleiche Anzahl und den gleichen Typ von Elementen aber jeweils unterschiedliche Werte haben)!
# Sorgen Sie dafür, dass die Tupel mindestens zwei Elemente haben!
#
# Lassen Sie nun Ihre Liste sortieren!
# Wie wird eine Liste von Tupeln sortiert?
#
# Experimentieren Sie mit Tupeln unterschiedlicher Größe oder unterschiedlichen/ähnlichen/teilweise gleichen Inhalts!
# Experimentieren Sie mit verschiedenen Typen für die Tupel-Elemente!
# Welches Kriterium kommt beim Sortieren wann zum Einsatz?
# +-+-+-+-+-+-+-+ +-+

tupel_liste = [(3, 5), (1, 7), (4, 2), (9, 1), (5, 4), (7, 3), (2, 8), (6, 0), (8, 6), (0, 9)]
tupel_liste.sort()
print("Sortierte Liste:", tupel_liste)

tupel_liste2 = [(3, 5), (1, 7, 9), (4, 2), (9, 1), (5, 4, 8), (7, 3)]
tupel_liste2.sort()
print("Sortierte Liste (unterschiedliche Größen):", tupel_liste2)

tupel_liste3 = [("Eierlikör", 3), ("Bier", 4), ("Cherry", 8), ("Aperol", 5), ("DunkelBier", 1)]
tupel_liste3.sort()
print("Sortierte Liste (unterschiedliche Typen):", tupel_liste3)


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |8|
# Buchstaben zählen
# Erstellen Sie eine Funktion buchstaben_anzahl, die einen String entgegennimmt und die darin enthaltenen Zeichen
# jeweils mit deren Häufigkeit im String als Liste von Tupeln zurückgibt. Dabei sollen Großbuchstaben wie
# Kleinbuchstaben behandelt werden. Die Tupel in der Liste sollen so sortiert sein, dass die Buchstaben der Tupel
# alphabetisch geordnet sind.
# +-+-+-+-+-+-+-+ +-+

def buchstaben_anzahl(text):
    a = list(text.lower())
    b = Counter(a)
    return str(list(b.items()))[1::][:-1]

print(buchstaben_anzahl('Erdbeereis'))


def buchstaben_anzahlII(text):
    a = text.lower()
    buchstaben_count = {}
    for char in a:
        if char in buchstaben_count:
            buchstaben_count[char] += 1
        else:
            buchstaben_count[char] = 1
    return sorted(buchstaben_count.items())

#print(buchstaben_anzahlII("Erdbeereis"))