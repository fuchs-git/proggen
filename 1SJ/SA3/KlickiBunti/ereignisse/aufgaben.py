# Erstellen Sie ein Fenster und einige Widgets Ihrer Wahl. Lassen Sie sowohl das Fenster als auch die Widgets auf
# verschiedene Ereignisse reagieren (Maus, Tastatur, Fenster). Lassen Sie sich in jeder Reaktion mindestens mit print
# die Art des Ereignisses und je nach Ereignis weitere Details ausgeben. Versuchen Sie zusätzlich, einzelne Widgets als
# Reaktion auf Ereignisse in Ihrer Darstellung zu verändern (Text ändern, Farbe ändern, Größe ändern, Position ändern …).
#
# Testen Sie verschiedene Kombinationen und Varianten. Spielen Sie!

import tkinter as tk

fenster = tk.Tk()
fenster.geometry("400x400")

lbl =[tk.Label(text=f'Label {i+1}', width=50, height=5) for i in range(5)]

for l in lbl:
    l.pack(padx=5, pady=10)

fenster.mainloop()