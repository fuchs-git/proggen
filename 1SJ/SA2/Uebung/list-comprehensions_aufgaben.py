# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |1|
# Erzeugen Sie eine Funktion ziffern_lc(n), die eine natürliche Zahl n übergeben bekommt und eine Liste der
# Ziffern von n zurückgibt. Beispiel: der Aufruf ziffern_lc(1234) soll [1, 2, 3, 4] zurückliefern.
# Lösen Sie die Aufgabe mit einer List-Comprehension in der Funktion!
# +-+-+-+-+-+-+-+ +-+


def ziffern_lc(n):
    return [int(x) for x in str(n)]


# print(ziffern_lc(1234))

# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |2|
# Erzeugen Sie eine Funktion listen_potenz_lc, die zwei Parameter übergeben bekommt.
# Eine Liste mit Zahlen und einen optionalen Exponenten der per default auf 2 gesetzt ist.
# Die Funktion gibt eine Liste zurück, in der die Elemente der Eingabeliste mit dem Exponenten potenziert wurden.
# Beispiel:
# Der Aufruf listen_potenz_lc([1, 2, 3.5, 15]) soll [1, 4, 12.25, 225] zurückliefern.
# Der Aufruf listen_potenz_lc([1, 2, 3.5, 15], 3) soll [1, 8, 42.875, 3375] zurückliefern.
# Lösen Sie die Aufgabe mit einer List-Comprehension in der Funktion!
# +-+-+-+-+-+-+-+ +-+
def listen_potenz_lc(liste, exp=2):
    return [x ** exp for x in liste]


# print(listen_potenz_lc([1, 2, 3.5, 15]))

# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |3|
# Erzeugen Sie eine Funktion listen_addition, die zwei gleich lange Listen mit Zahlen übergeben bekommt
# (Sie dürfen sich darauf verlassen, dass die Listen gleich lang sind) und eine Liste der paarweisen Summen der
# jeweiligen Eingabelisten-Elemente zurückgibt. Der Aufruf listen_addition([1, 2, 3.5], [4, 5.4, 1.1]) soll
# [5, 7.4, 4.6] zurückliefern. Lösen Sie die Aufgabe mit einer List-Comprehension in der Funktion!
# +-+-+-+-+-+-+-+ +-+

def listen_addition(a, b):
    return [a[i] + b[i] for i in range(len(a))]


# print(listen_addition([1, 2, 3.5], [4, 5.4, 1.1]))

# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |4|
# Erzeugen Sie eine Liste aller dreistellige Zahlen, deren dritte Ziffer die Summe der ersten beiden Ziffern ist!
# Lösen Sie die Aufgabe mit einer List-Comprehension!
# +-+-+-+-+-+-+-+ +-+

print([x for x in range(100, 1000) if int(str(x)[2]) == int(str(x)[0]) + int(str(x)[1])])


# +-+-+-+-+-+-+-+ +-+
# |A|u|f|g|a|b|e| |5|
# +-+-+-+-+-+-+-+ +-+


# print( [ziffern_lc(x) for x in range(10,500)  ])
# for i in range(10,2646798):
#     liste = ziffern_lc(i)
#     summe = 0
#     for ziffer in range(len(liste)):
#         summe += liste[ziffer]**(ziffer+1)
#     if summe == i:
#         print(i, summe)
#     summe = 0


# for exponent, ziffer  in enumerate(ziffern_lc(123)):
#     print(ziffer ** (exponent+1))

def test(i):
    return sum([ziffer ** (exponent + 1) for exponent, ziffer in enumerate([int(y) for y in str(i)])])

# print([test(x) for x in range(10, 2646799) if x == test(x)])



print([sum([ziffer ** (exponent + 1) for exponent, ziffer in enumerate([int(y) for y in str(x)])]) for x in range(10, 2646799) if x == sum([ziffer ** (exponent + 1) for exponent, ziffer in enumerate([int(y) for y in str(x)])])])
