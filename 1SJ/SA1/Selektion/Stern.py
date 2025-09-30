import turtle

def stern(anzahl_zacken):
    erlaubt = [3, 5, 7, 9, 11]
    if anzahl_zacken in erlaubt:
        for i in range(anzahl_zacken):
            turtle.forward(100)
            turtle.left(180 - 180 / anzahl_zacken)
    else:
        turtle.write(f'Die folgenden Zahlen sind: {erlaubt} erlaubt!')

stern(11)
