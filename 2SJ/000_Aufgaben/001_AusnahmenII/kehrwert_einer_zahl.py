# Schreiben Sie ein Programm, das den Benutzer nach einer ganzen Zahl fragt und dann den Kehrwert dieser Zahl berechnet
# (also 1 geteilt durch die eingegebene Zahl). Beachten Sie dabei folgende Anforderungen:

def programm():
    try:
        i = int(input('Ich frage dich nach einer Zahl:'))
        e = 1/i
    except ValueError:
        print(f'Fehler: Ungültige Eingabe. Bitte geben Sie eine ganze Zahl ein.')
        exit()
    except ZeroDivisionError:
        print("Fehler: Division durch Null ist nicht erlaubt.")
        exit()
    else:
        print(f"Der Kehrwert von {i} ist {e}.")
    finally:
        print('Programm wurde beendet.')

programm()