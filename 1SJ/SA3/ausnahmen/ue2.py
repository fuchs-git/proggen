# Variante 1 mit zusätzlichem Fehler
while True:  # Endlosschleife, die wir mit break verlassen, sobald wir ein int haben
    x = input("Geben Sie eine ganze Zahl ein: ")
    if  x[0] in '+-0123456789' and x[1:].isdigit():
        x = int(x)  # das sollte nicht mehr schief gehen (oder doch?)
        break  # wir haben ein int, raus aus der Schleife
    else:
        print("Das war keine ganze Zahl! Noch ein Versuch...")
print(f"Es wurde {x} eingegeben")