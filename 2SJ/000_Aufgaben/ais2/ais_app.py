import tkinter as tk
from datetime import datetime
import datenmodell

from datenmodell import schiffstypen, Schiff


def listbox_select(event: tk.Event):
    for lbl in daten_labels:
        lbl.destroy()
    daten_labels.clear()

    mmsi = lb_ships.get(lb_ships.curselection()[0])

    schiff = schiffe[mmsi]
    print(schiff)

    schiffs_daten.set(f"{schiff} - Fahrstrecke {schiff.fahrstrecke():0.1f}km")

    for datenpunkt in schiff.datenpunkte:
        x, y = lat_lon_nach_x_y(float(datenpunkt.lat), float(datenpunkt.lon))

        # die Darstellung mit Labels ist langsam aber geht
        lbl = tk.Label(master=lbl_karte, text='x', font='courier, 3', bg="blue", borderwidth=0)
        daten_labels.add(lbl)  # die SuS-taugliche Variante muss sich die Labels merken
        lbl.place(x=x, y=y)


def lat_lon_nach_x_y(lat: float, lon: float) -> tuple:
    """
    berechnet die Pixel-Koordinate (x,y) aus gegebener geografischer Breite und Länge
    :param lat: Latitude - geografische Breite, also wie weit nördlich (+) oder südlich (-)
    :param lon: Longitude - geografische Länge, also wie weit westlich (-) oder östlich (+)
    :return: Tupel (x,y) - die x- und die y-Koordinate, jeweils als int
    """
    return (int(1458.23 * (lon + 74.191)),
            int(1934.36 * (40.855 - lat)))

# Schiffsdaten einlesen

dateiname_daten = "AIS_2024_05_29_newyork.csv"

ais_db = datenmodell.Datenbank('password', setup=False)
#schiffe = ais_db.csv_einlesen(dateiname_daten)
schiffe = ais_db.schiffe()


# ----------- GUI -----------
fenster = tk.Tk()
# das genaue Layout soll so sein:
# unten ein Label mit der Beschreibung des gewählten Schiffs
# darüber links eine Listbox aller Schiffe und rechts ein Label, welches als Karte dient

schiffs_daten = tk.StringVar()
tk.Label(textvariable=schiffs_daten).pack(side=tk.BOTTOM, padx=15, pady=15)

lb_ships = tk.Listbox(fenster, height=31, justify=tk.CENTER)
lb_ships.pack(side=tk.LEFT)

image = tk.PhotoImage(file="newyork_karte.png")

lbl_karte = tk.Label(image=image)
lbl_karte.pack(side=tk.LEFT)

lb_ships.insert(tk.END, *sorted(schiffe.keys()))

# GUI - Karte bei Auswahl füllen
daten_labels = set()
lb_ships.bind('<<ListboxSelect>>', listbox_select)

fenster.mainloop()

