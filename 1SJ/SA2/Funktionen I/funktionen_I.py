
# -----------------------------------------------------------------------------------------------------
# 1. Hallo Python!- Funktion
# -----------------------------------------------------------------------------------------------------
#
# def begrusse_python():
#     print('Hallo Python!')
#
# begrusse_python()



# -----------------------------------------------------------------------------------------------------
# 2. Hallo Python!- Funktion anders
# -----------------------------------------------------------------------------------------------------

# def begrusse_python():
#     return ('Hallo Python!')
#
#
# print(begrusse_python())

# -----------------------------------------------------------------------------------------------------
# 3. Begrüßungs-Funktion
# -----------------------------------------------------------------------------------------------------

def begruessen(name="Welt"):
    return f'Hallo {name}!'

# print(begruessen("Tim"))

# -----------------------------------------------------------------------------------------------------
# 4.Ergänzung einer Beschreibung
# -----------------------------------------------------------------------------------------------------

def sparbetrag(einlage: float, zinssatz: float = 0.03, jahre: int = 1) -> float:
    for i in range(jahre):
        einlage += einlage * zinssatz
    return einlage


# print(sparbetrag(1000))                     # Sparbetrag zum gegebenen Zinssatz von 3% für ein Jahr
# print(sparbetrag(1000, zinssatz=0.04))      # Sparbetrag zum gegebenen Zinssatz von 4% für ein Jahr
# print(sparbetrag(1000, jahre=20))           # Sparbetrag zum gegebenen Zinssatz von 3% für 20 Jahre
# print(sparbetrag(1000, 0.04, 20))


# -----------------------------------------------------------------------------------------------------
# 5.Eine einfache Funktion
# -----------------------------------------------------------------------------------------------------

def nachfolger(i):
    try:
        return i + 1
    except:
        return "Das war keine Zahl"

# print(nachfolger(9))


# -----------------------------------------------------------------------------------------------------
# 6. Funktion mit vorbelegten Parametern
# -----------------------------------------------------------------------------------------------------

def volumen(n:int, d:int=3) -> int:
    return n** d


# print(volumen(5))


# -----------------------------------------------------------------------------------------------------
# 7. Summe
# -----------------------------------------------------------------------------------------------------

def summe(zahl):
    pass
