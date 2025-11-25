import tkinter as tk
from filmDatabase import filme


def filmauswahl(event:tk.Event):
    auswahl =lbox.get(lbox.curselection())

    for film, name, vorname, bj in filme.regisseur():
        if str(auswahl) == film:
            regisseurlabel.configure(text=f'{vorname} {name} ({bj})')

    for _, name, jahr, monat in filme.filme():
        if str(auswahl) == name:
            filmlabel.configure(text=name)
            erscheinungsjahrlabel.configure(text=jahr)
            darsteller = []
            for film, nachname, vorname, rolle in filme.schauspieler():
                if film == name:
                    darsteller.append(f'{vorname} {nachname} als {rolle}\n')
            text = ""
            for x in darsteller:
                text += x
            schauspielerlabel.configure(text=text)



def suche(event):
    ...


def suche_resetten(event):
    ...


fenster = tk.Tk()
fenster.title("Super App")
fenster.geometry("550x400")

frameoben = tk.Frame(fenster)
frameoben.pack()
framelinks = tk.Frame(fenster)
framelinks.pack(side="left", fill="y", padx=10, pady=10)
framerechts = tk.Frame(fenster)
framerechts.pack(side="right", fill="both", expand=True, padx=10, pady=10)
tk.Label(framelinks, text="Filme:").pack(side="top")

############# Aufgabe 4 ################

lbox = tk.Listbox(framelinks, width=35)
lbox.pack(side="top")

for _, name, jahr, monat in filme.filme():
    lbox.insert("end", name)

lbox.bind("<<ListboxSelect>>", filmauswahl)

######## Aufgabe 5 #######

tk.Label(framerechts, text="Titel:", anchor="w").pack(fill="x")
filmlabel = tk.Label(framerechts, anchor="w")
filmlabel.pack(fill="x")
tk.Label(framerechts).pack()

tk.Label(framerechts, text="Erscheinungsjahr:", anchor="w").pack(fill="x")
erscheinungsjahrlabel = tk.Label(framerechts, anchor="w")
erscheinungsjahrlabel.pack(fill="x")
tk.Label(framerechts).pack()

tk.Label(framerechts, text="Regisseur:", anchor="w").pack(fill="x")
regisseurlabel = tk.Label(framerechts, anchor="w")
regisseurlabel.pack(fill="x")
tk.Label(framerechts).pack()

tk.Label(framerechts, text="Schauspieler:", anchor="w").pack(fill="x")
schauspielerlabel = tk.Label(framerechts, anchor="w", justify="left")
schauspielerlabel.pack(fill="x")
tk.Label(framerechts).pack()

suchfeld = tk.Entry(frameoben)
suchfeld.pack()
suchfeld.bind("<KeyRelease>", suche)
suchfeld.bind("<Return>", suche_resetten)

fenster.mainloop()
