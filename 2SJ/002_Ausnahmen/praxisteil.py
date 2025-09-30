try:
    kinder = int(input("Sie haben 5 Äpfel. Geben Sie ein,"
                       " wie viele Kinder sich diese Äpfel teilen sollen: "))
    anteil_pro_kind = 5 / kinder
    print(f"Jedes Kind bekommt {anteil_pro_kind:.2f} Äpfel")
except ZeroDivisionError:
    print("unter 0 Kindern kann man die Äpfel nicht aufteilen")
else:
    print("Die Berechnung hat ohne Fehler geklappt")
finally:
    print("Esst mehr Äpfel!")