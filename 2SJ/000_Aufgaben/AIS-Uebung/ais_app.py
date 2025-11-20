import tkinter as tk
from datetime import datetime

from datenmodell import schiffstypen, Schiff


def listbox_select(event: tk.Event):
    for lbl in daten_labels:
        lbl.destroy()
    daten_labels.clear()

    mmsi = lb_ships.get(lb_ships.curselection()[0])

    schiff = schiffe[mmsi]

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


################################################################################
# TODO auf Datenbank umbauen
# Dieser Teil hier muss auf DB umgebaut werden
################################################################################

# Schiffsdaten einlesen
schiffe = {}
dateiname_daten = "AIS_2024_05_29_newyork.csv"
try:
    with open(dateiname_daten) as file:
        print(file.readline())  # erste Zeile weglassen (Header)
        for zeile in file:

            # MM, Time, LAT, LON, S, C, H, Name, I, C, Typ, S, Length, Width,Draft,Cargo,TransceiverClass
            mmsi, zeit, lat, lon, _, _, _, name, _, _, typ, *_ = zeile.split(",")

            if mmsi not in schiffe:
                # Es gibt Zeilen in denen der Typ kaputt ist
                typ = int(typ) if typ else 99
                schiffe[mmsi] = Schiff(mmsi, name, schiffstypen[typ])
            schiffe[mmsi].datenpunkt_hinzufuegen(datetime.strptime(zeit, "%Y-%m-%dT%H:%M:%S"), float(lat), float(lon))
except FileNotFoundError:
    print(f"Datei {dateiname_daten} nicht gefunden")
except OSError:
    print(f"Fehler beim Lesen der Datei {dateiname_daten}")

print("A3: Vor extra-Filterung:", len(schiffe), "\n")  # Vergleichslösung

# extra Datenfilter
# Alle Schiffe weglassen, die weniger als 10 oder über 500 Datenpunkte haben
# das ist evtl. Tricky, wenn man versucht das original-dict zu verändern
# Ersatzlösung: nicht filtern
schiffe = {mmsi: schiff
           for mmsi, schiff in schiffe.items()
           if 10 <= len(schiff.datenpunkte) <= 500}

################################################################################


# GUI
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

