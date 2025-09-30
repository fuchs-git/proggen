'''
Erstellen Sie ein Modul namens mathe_operationen.py, das die Funktionen addieren(), subtrahieren(), multiplizieren() und dividieren() enthält.

    Importieren Sie dieses Modul in einem anderen Skript und verwenden Sie die Funktionen.

    Erweitern Sie das Modul mathe_operationen.py um die Python-Dokumentation. (->DOKU<-)

    Erweitern Sie das Modul um die Klasse Strichrechnung. Diese Klasse soll die Methoden addieren und subtrahieren enthalten.
    Was stellen Sie fest, wenn nun die Methode addieren aufgerufen wird? Was müssen Sie dafür alles tun?

    Erstellen Sie eine Variable mit dem Namen pi und weisen ihr den Wert 9 zu. Im nächsten Schritt importieren Sie in Ihr Testskript zusätzlich das Modul math. Welche pi-Variable wird genommen und ist das immer so?
'''
import math

class Strichrechnung:
    def __init__(self,a ,b):
        self.a = a
        self.b = b

    def addieren(self):
        return self.a + self.b

    def subtrahieren(self):
        return self.a - self.b


def addieren(a,b):
    return a+b

def subtrahieren(a,b):
    return a-b

def multiplizieren(a,b):
    return a*b

def dividieren(a,b):
    return a/b
