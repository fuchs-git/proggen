import os

with open("wortSpielereiListe.txt", "r") as f:
    liste = f.readlines()


# -------------------------------------------------------------------------------------------------------------
# Lassen Sie die Wortliste und die Länge der Liste ausgeben.
# -------------------------------------------------------------------------------------------------------------

# print(liste)
# print(len(liste))


# -------------------------------------------------------------------------------------------------------------
# Erzeugen Sie eine Funktion, die das längste Wort einer ihr übergebenen Liste von Worten zurückgibt!
#
# Geben Sie das längste Wort Ihrer Wortliste aus!
#
# Geben Sie das kürzeste Wort Ihrer Wortliste aus!
# -------------------------------------------------------------------------------------------------------------

def wortSpielerei(liste) -> liste:
    """
    Empfängt eine Liste und gibt eine Liste zurück.
    :return: längtstes Wort; Zeichenanzahl; kürzestes Wort; Zeichenanzahl
    """
    lwort, lzeichen = 0, 0
    kwort, kzeichen = 0, 1000
    for i in liste:
        i = i.strip()
        if len(i) > lzeichen:
            lzeichen = len(i)
            lwort = i
        elif len(i) < kzeichen:
            kzeichen = len(i)
            kwort = i
    return [lwort, lzeichen, kwort, kzeichen]


# print(f'Das längste Wort in der Liste ist "{wortSpielerei(liste)[0]}".')
# print(f'Das Wort hat insgesamt {wortSpielerei(liste)[1]} Zeichen.')
# print(f'Das kürzeste Wort in der Liste ist "{wortSpielerei(liste)[2]}".')
# print(f'Das Wort hat insgesamt {wortSpielerei(liste)[3]} Zeichen.')

# -------------------------------------------------------------------------------------------------------------
# Erzeugen sie eine Funktion, die überprüft, ob ein ihr übergebener String ein Palindrom ist! Ein Palindrom ist ein Text, der vorwärts und rückwärts gelesen gleich ist.
# Bauen Sie die Funktion so, dass Groß-/Kleinschreibung der Buchstaben ignoriert wird.
#
# Testen Sie Ihre Funktion an den Strings A, Affe, Anna und Reliefpfeiler.
#
# Geben Sie alle Worte Ihrer Wortliste aus, die ein Palindrom sind.
# -------------------------------------------------------------------------------------------------------------
def kill_sonderzeichen(x) -> str:
    wort = ""
    for char in x:
        if char.isalpha():
            wort += char
    return wort


def palindrom(liste):
    for i in liste:
        k = kill_sonderzeichen(i)
        if k.lower() == k[::-1].lower():
            print(i.strip())


# palindrom(liste)

# -------------------------------------------------------------------------------------------------------------
# Schreiben Sie eine Funktion, die eine gegebenen Liste "säubert". "Sauber" ist eine Liste, wenn Folgendes erfüllt ist:
#
#     alle Elemente der Liste sind Strings
#     alle Buchstaben sind in Kleinbuchstaben umgewandelt worden
#     kein Listenelement ist doppelt
#
# Erzeugen Sie eine neue "gesäuberte" Wortliste aus Ihrer alten Liste!
# -------------------------------------------------------------------------------------------------------------

def cleaner(liste):
    sauber = []
    for i in liste:
        i = str(i.strip().lower())
        if i not in sauber:
            sauber.append(i)
    return sauber


# print(cleaner(liste))

# -------------------------------------------------------------------------------------------------------------
# Schreiben Sie eine Funktion, die prüft, ob von zwei übergebenen Strings der Erste im zweiten vorkommt.
# Dabei soll Groß-/Kleinschreibung ignoriert werden.
#
# Testen Sie Ihre Funktion mit den beiden Strings Instinkt und Urinstinkt.
# -------------------------------------------------------------------------------------------------------------

def insideYou(a, b):
    for char in a:
        if char.lower() in b.lower():
            print(char)


# insideYou("Insekt", "Urinstinkt")

# -------------------------------------------------------------------------------------------------------------
# Geben Sie zeilenweise jedes Wort der gesäuberten Wortliste aus, welches mindestens ein anderes Wort der
# gesäuberten Wortliste enthält! Dabei sollen zusätzlich hinter jedem Wort alle enthaltenen Worte angegeben werden.
# Es ist natürlich nicht sehr sinnvoll, ein Wort auszugeben, das sich selbst enthält (das trifft ja für jedes Wort zu).
# Beispiel, wie eine Zeile für ein Wort aussehen könnte: "because" enthält "a" "be" "s" "u" "use"
# -------------------------------------------------------------------------------------------------------------

def deepInside(liste_a:list, liste_b:list):
    ausgabe = []
    for suchwort in liste_a:
        speicher = []
        liste_b.remove(suchwort)
        for wort in liste_b:
            if wort in suchwort:
                speicher.append(wort)
        if len(speicher) != 0:
            speicher.insert(0, suchwort)
            ausgabe.append(speicher)
        liste_b.append(suchwort)
    return ausgabe


a = deepInside(cleaner(liste), cleaner(liste))


def deepAusgabe(a):
    for i in a:
        for x in range(len(i)):
            match x:
                case 0:
                    print(f'"{i[x]}" enthält ', end=' ')
                case _:
                    print(f'"{i[x]}"', end=' ')
        print()


# deepAusgabe(a)

# -------------------------------------------------------------------------------------------------------------
# 2. Ziffern
# Erzeugen Sie eine Funktion ziffern(n), die eine natürliche Zahl n übergeben bekommt und eine Liste
# der Ziffern von n zurückgibt.
#
# Beispiel: Der Aufruf ziffern(1234) soll [1, 2, 3, 4] zurückliefern.
# -------------------------------------------------------------------------------------------------------------

def ziffern(n: int):
    buffer = list()
    in_string = str(n)
    for buchstabe in in_string:
        buffer.append(int(buchstabe))
    return buffer


# print(ziffern(1234))

def ziffern2(n):
    string_liste = list(str(n))
    int_liste = [int(zeichen) for zeichen in string_liste]
    return int_liste


# print(ziffern2(12345))


# -------------------------------------------------------------------------------------------------------------
# 3. Listensumme
# Erzeugen Sie eine Funktion listen_summe(n), die eine Liste mit Zahlen übergeben bekommt und die Summe der Zahlen zurückgibt.
#
# Beispiel:
# Der Aufruf listen_summe([1, 2, 3, 4]) soll 10 zurückliefern.
# -------------------------------------------------------------------------------------------------------------

def listen_summe(int_liste):
    return sum([i for i in int_liste])#<----- was soll das keine original summenfunktion


# print(listen_summe([1,2,3,4]))

# -------------------------------------------------------------------------------------------------------------
# 4. Listen-Potenz
# Erzeugen Sie eine Funktion listen_potenz, die zwei Parameter übergeben bekommt. Eine Liste mit Zahlen und einen
# optionalen Exponenten, der per Default auf 2 gesetzt ist. Die Funktion gibt eine Liste zurück, in der die Elemente
# der Eingabeliste mit dem Exponenten potenziert wurden.
#
# Beispiel:
# Der Aufruf listen_potenz([1, 2, 3.5, 15]) soll [1, 4, 12.25, 225] zurückliefern.
# Der Aufruf listen_potenz([1, 2, 3.5, 15], 3) soll [1, 8, 42.875, 3375] zurückliefern.
# -------------------------------------------------------------------------------------------------------------

def listen_potenz(float_liste, exponent=2):
    return [i ** exponent for i in float_liste]


# print(listen_potenz([1,2,3.5,15],3))

# -------------------------------------------------------------------------------------------------------------
# 5. Listen-Addieren
# Erzeugen Sie eine Funktion listen_addition, die zwei gleich lange Listen mit Zahlen übergeben bekommt
# (Sie dürfen sich darauf verlassen, dass die Listen gleich lang sind) und eine Liste der paarweisen Summen der
# jeweiligen Eingabelisten-Elemente zurückgibt.
#
# Beispiel:
# Der Aufruf listen_addition([1, 2, 3.5], [4, 5.4, 1.1]) soll [5, 7.4, 4.6] zurückliefern.
# -------------------------------------------------------------------------------------------------------------

def listen_addition(list_a, list_b):
    x = []
    for i in range(len(list_a)):
        x.append(list_a[i] + list_b[i])
    return x


# print(listen_addition([1, 2, 3.5], [4, 5.4, 1.1]))


# -------------------------------------------------------------------------------------------------------------
# 6. Ziffernsummen
# Erzeugen Sie eine Liste aller dreistelligen Zahlen, deren dritte Ziffer die Summe der ersten beiden Ziffern ist!
# -------------------------------------------------------------------------------------------------------------

def ziffernsummen():
    for i in range(100, 1000):
        x = str(i)
        if int(x[0]) + int(x[1]) == int(x[2]):
            print(f'{i}, ', end='')
    print('\b\b')


# ziffernsummen()

# -------------------------------------------------------------------------------------------------------------
# 7. Narzisstische Zahlen
# Narzisstische Zahlen sind genau die Zahlen, die sich als Summe ihrer Ziffern, jeweils potenziert mit der Länge
# der Zahl, darstellen lassen. (nochmal mit anderen Worten: jede der Ziffern einzeln für sich hoch die Länge der Zahl
# und das Ganze zusammengezählt ergibt wieder die Zahl)
#
# Beispiel:
# Die dreistellige Zahl 407 lässt sich schreiben als:
#  407 = 4^3 + 0^3 + 7^3 = 64 + 0 + 343
# Noch ein Beispiel:
# Die fünfstellige Zahl 54748 lässt sich schreiben als:
# Erzeugen Sie eine Liste mit 15 narzisstischen Zahlen größer als 10!
# -------------------------------------------------------------------------------------------------------------

def narzisstische_zahlen():
    for zahl in range(99000000):
        summen_liste = []
        x = str(zahl)
        for ziffer in x:
            summen_liste.append(int(ziffer) ** len(x))
        summe = sum([x for x in summen_liste])
        if zahl == summe:
            print(f'{x} = ', end='')
            for i in x:
                print(f'{i}^{len(x)}  + ', end='')
            print('\b\b\b= ', end='')
            for i in summen_liste:
                print(f'{i}  + ', end='')
            print('\b\b')



# narzisstische_zahlen()

# -------------------------------------------------------------------------------------------------------------
# 8. Römische Zahlen
# Sicherlich kennen Sie die römischen Zahlen. Diese lassen sich natürlich mit Python in die und aus den
# arabischen Zahlen, wie wir sie für gewöhnlich benutzen, erzeugen.
#
# Erzeugen Sie eine Funktion arabisch_zu_roemisch, die eine Zahl als Integer übergeben bekommt und einen String, der
# die entsprechende römische Zahl darstellt, zurückliefert! Die Funktion sollte auch überprüfen, ob die Eingabe gültig
# ist (eine natürliche Zahl größer 0) und eine Fehlermeldung ausgeben, wenn dies nicht der Fall ist. In so einem Fall
# bietet sich als Rückgabewert der Funktion ein leerer String an. Des Weiteren ist es ab einer gewissen Größe der
# Eingabe nicht mehr sehr sinnvoll, diese in eine römische Zahl umzuwandeln, sie können (müssen aber nicht) hier eine
# Obergrenze festlegen (z.B. bei 5000 oder bei 10000).
# -------------------------------------------------------------------------------------------------------------


def arabisch_zu_roemisch(zahl:int):
    rom = ''
    while zahl > 0:
        if   zahl >= 1000: zahl -= 1000; rom += 'M'
        elif zahl >= 900:  zahl -= 900;  rom += 'CM'
        elif zahl >= 500:  zahl -= 500;  rom += 'D'
        elif zahl >= 400:  zahl -= 400;  rom += 'CD'
        elif zahl >= 100:  zahl -= 100;  rom += 'C'
        elif zahl >= 90:   zahl -= 90;   rom += 'XC'
        elif zahl >= 50:   zahl -= 50;   rom += 'L'
        elif zahl >= 40:   zahl -= 40;   rom += 'XL'
        elif zahl >= 10:   zahl -= 10;   rom += 'X'
        elif zahl >= 9:    zahl -= 9;    rom += 'IX'
        elif zahl >= 5:    zahl -= 5;    rom += 'V'
        elif zahl >= 4:    zahl -= 4;    rom += 'IV'
        elif zahl >= 1:    zahl -= 1;    rom += 'I'
    return rom

print(arabisch_zu_roemisch(1503))

# -------------------------------------------------------------------------------------------------------------
# Erzeugen Sie eine Funktion roemisch_zu_arabisch, die eine römische Zahl als String übergeben bekommt und ein Integer,
# das die entsprechende arabische Zahl darstellt, zurückliefert!
# -------------------------------------------------------------------------------------------------------------

def roemisch_zu_arabisch(text):
    rom = list(text)
    arab = 0
    while len(rom) != 0:
        if rom[0]   == "M": arab += 1000;   rom.pop(0)
        elif rom[0] == "C" and len(rom) >1 and rom[1] == 'M': arab += 900;  rom.pop(0); rom.pop(0)
        elif rom[0] == "C" and len(rom) >1 and rom[1] == 'D': arab += 400;  rom.pop(0); rom.pop(0)
        elif rom[0] == "X" and len(rom) >1 and rom[1] == 'C': arab += 90;   rom.pop(0); rom.pop(0)
        elif rom[0] == "X" and len(rom) >1 and rom[1] == 'L': arab += 40;   rom.pop(0); rom.pop(0)
        elif rom[0] == "I" and len(rom) >1 and rom[1] == 'X': arab += 9;    rom.pop(0); rom.pop(0)
        elif rom[0] == "I" and len(rom) >1 and rom[1] == 'V': arab += 4;    rom.pop(0); rom.pop(0)
        elif rom[0] == "D" : arab += 500;   rom.pop(0)
        elif rom[0] == "C" : arab += 100;   rom.pop(0)
        elif rom[0] == "L" : arab += 50;    rom.pop(0)
        elif rom[0] == "X" : arab += 10;    rom.pop(0)
        elif rom[0] == "V" : arab += 5;     rom.pop(0)
        elif rom[0] == "I" : arab += 1;     rom.pop(0)
    return arab

def rom_zu_arabII(text):
    for i in range(1,100000):
        if arabisch_zu_roemisch(i) == text:
            return i
    print("Angegebener Text ist keine Zahl")
    return -1

print(roemisch_zu_arabisch("MDIII"))
print(rom_zu_arabII("MDIII"))


# -------------------------------------------------------------------------------------------------------------
# 3. Finden Sie die Zahl kleiner 1000, deren Zahldarstellung als römische Zahl am längsten ist!
# -------------------------------------------------------------------------------------------------------------
rom = ''
laenge = 0
for i in range(1000):
    if len(arabisch_zu_roemisch(i)) > laenge:
        rom = arabisch_zu_roemisch(i)
        laenge = len(arabisch_zu_roemisch(i))
# print(rom)

# -------------------------------------------------------------------------------------------------------------
# 4. Wenn man alle(!) römischen Zahlen alphabetisch sortiert aufschreibt,
# wird es eine erste und eine letzte Zahl in der Liste geben.
# -------------------------------------------------------------------------------------------------------------

rom_liste = list()
for i in range(1,1000):
    rom_liste.append(arabisch_zu_roemisch(i))
# print(f'Erste Zahl = {sorted(rom_liste)[0]}, letzte Zahl = {sorted(rom_liste)[-1]}')


