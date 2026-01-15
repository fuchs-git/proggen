import re

eingabe = input("Eingabe:")
pattern = r"^[a-zA-Z][a-zA-Z0-9+_.%&!#-]*@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,})$"
ergebnis = re.match(pattern, eingabe)
if ergebnis:
    print(eingabe, "ist korrekt")
else:
    print(eingabe, "ist nicht korrekt")