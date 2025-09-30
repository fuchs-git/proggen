class Buch:
    def __init__(self, titel: str, jahr: str, autor: 'Autor'):
        self.titel = titel
        self.jahr = jahr
        self.autor = autor

    def __str__(self):
        return f'{self.titel}'

    def __eq__(self, other: 'Buch'):
        return self.titel == other.titel

    def __hash__(self):
        return hash(self.titel)


class Autor:
    def __init__(self, name):
        self.name = name
        self.buch_set = set()

    def add_buch(self, buch: Buch):
        self.buch_set.add(buch)

    def __repr__(self):
        return f'{self.name}'

    def __hash__(self):
        return hash(self.name)


with open('bibliothek_autoren_buecher.csv', 'r') as f:
    f.readline()
    books = f.read().splitlines()
    verschiedene_buecher = len(books)

autoren_dict = {}
tmp = {}

for book in books:
    id, autor_name, titel, jahr = book.split(';')
    autor_obj = tmp.get(autor_name)
    if not autor_obj:
        autor_obj = Autor(autor_name)
        tmp[autor_name] = autor_obj
        autoren_dict[autor_obj] = autor_obj

    buch_obj = Buch(titel, jahr, autor_obj)
    autor_obj.add_buch(buch_obj)

for autor in autoren_dict:
    print(f'{autor.name}: {[buch.titel for buch in autor.buch_set]}')

anzahl_autoren = len(autoren_dict)
anzahl_alle_buecher = sum(len(autor.buch_set) for autor in autoren_dict)

# GUI
import tkinter as tk

fenster = tk.Tk()
fenster.geometry("800x400")
fenster.title("Autoren und Bücher")

# Statistik-Anzeige oben
info_label = tk.Label(fenster, text=(
    f"Anzahl Autoren: {anzahl_autoren} | "
    f"Gesamtanzahl Bücher: {anzahl_alle_buecher} | "
    f"Verschiedene Buchtitel: {verschiedene_buecher}"
))
info_label.pack(pady=10)

# Frames für Listenansicht
frame_links = tk.Frame(fenster)
frame_rechts = tk.Frame(fenster)
frame_links.pack(side="left", expand=True, fill="both")
frame_rechts.pack(side="right", expand=True, fill="both")

# Listboxen
listbox_autoren = tk.Listbox(frame_links)
listbox_buecher = tk.Listbox(frame_rechts)
listbox_autoren.pack(expand=True, fill="both")
listbox_buecher.pack(expand=True, fill="both")

# Autoren sortiert einfügen
autorenliste = sorted(autoren_dict, key=lambda x: x.name)
for autor in autorenliste:
    listbox_autoren.insert("end", autor.name)


# Event-Funktion für Auswahl
def autor_ausgewaehlt(event):
    auswahl = listbox_autoren.curselection()
    if not auswahl:
        return
    index = auswahl[0]
    autor_name = listbox_autoren.get(index)

    for autor in autoren_dict:
        if autor.name == autor_name:
            listbox_buecher.delete(0, "end")
            for buch in sorted(autor.buch_set, key=lambda b: b.jahr):
                listbox_buecher.insert("end", f"{buch.titel} ({buch.jahr})")
            break


listbox_autoren.bind("<ButtonRelease-1>", autor_ausgewaehlt)

fenster.mainloop()
