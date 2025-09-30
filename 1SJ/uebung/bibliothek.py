import tkinter as tk
from tkinter import filedialog


class Autor:
    def __init__(self, name: str, buecher: set):
        self.name = name
        self.buecher = buecher

    def __repr__(self):
        return f'Autor: {self.name}'


class Buch:
    def __init__(self, ID: str, Titel: str, Jahr, Autor:str):
        self.id = ID
        self.titel = Titel
        self.jahr = Jahr
        self.autor = Autor

    def __repr__(self):
        return f'Buch: {self.titel} von {self.autor}\n'

    def __eq__(self, other):
        return isinstance(other, Buch) and self.titel == other.titel and self.autor == self.autor

    def __hash__(self):
        return hash(self.titel and self.autor)


def open_file():
    global filename
    global buecher
    while filename == '':
        filename = filedialog.askopenfilename(
            filetypes=[("Text-Dateien", "*.csv")],
            title="Wähle eine CSV-Datei aus",
        )
    with open(filename, 'r') as f:
        f.readline()
        alles = f.read()
    buecher = alles.split('\n')
    magic(buecher)
    return filename


def magic(buecher):
    global buecher_liste
    for buch in buecher:
        b = buch.split(';')
        id, autor, titel, jahr = b
        buecher_liste.append(Buch(id,titel,jahr,autor))



filename = ''
buecher = []
buecher_liste = []



fenster = tk.Tk()
fenster.geometry('500x300')

btn = tk.Button(text='Datei öffnen', command=open_file)
btn.pack(padx="10px", pady="10px")

fenster.mainloop()
print(*buecher_liste)

