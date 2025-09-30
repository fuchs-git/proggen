import tkinter as tk
from tkinter import filedialog



# Um den Inhalt der Datei zu analysieren, sind vorab die Klassen Autor und Buch anzulegen
class Autor:
    """
    Ein Autor kennt seinen Namen (str) und seine Bücher (Set!), die Bücher werden aber erst später dem Autor hinzugefügt.
    """
    def __init__(self, name:str):
        self.buecher = set()
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def __eq__(self, other:'Autor'):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

class Buch:
    """
    Das Buch kennt seine ID (str), den Titel (str), den Autor (Autor) und das Jahr (str) der Auflage
    """
    def __init__(self, id:str,titel:str, autor:Autor, jahr:str):
        self.id = id
        self.titel = titel
        self.autor = autor
        self.jahr = jahr

    def __repr__(self):
        return f'{self.id}, {self.titel}, {self.autor}, {self.jahr}'

    def __eq__(self, other: 'Buch'):
        return self.titel == other.titel and self.autor == other.autor

    def __hash__(self):
        return hash((self.titel, self.autor))

def analysiere_datei():

    # Datei einlesen
    filename = filedialog.askopenfilename(
        filetypes=[("Text-Dateien", "*.csv")],
        title="Wähle eine CSV-Datei aus",
    )
    try:
        with open(filename, 'r') as f:
            f.readline()
            books = f.read().splitlines()
    except OSError:
        print("Fehler beim Import!")

    #
    autoren_set = set()
    buecher_liste = []
    for book in books:
        id, autor, buch, jahr = book.split(';')

        autor_obj = Autor(autor)
        if autor_obj not in autoren_set:
            autoren_set.add(autor_obj)
        else:
            for a in autoren_set:
                if a.name == autor:
                    autor_obj = a
                    break

        buecher_liste.append(Buch(str(id), str(buch), autor_obj, str(jahr)))
        autor_obj.buecher.add(Buch(str(id), str(buch), autor_obj, str(jahr)))
    # statistik
    # Auswertung erzeugen
    anzahl_autoren = len(autoren_set)
    anzahl_buecher = len(buecher_liste)
    anzahl_verschiedene_buecher = len(set(buecher_liste))

    # Ergebnistext
    info_text = (
        f"Anzahl Autoren: {anzahl_autoren} "
        f"Gesamtanzahl Bücher: {anzahl_buecher} "
        f"Verschiedene Bücher: {anzahl_verschiedene_buecher}"
    )
    info_label = tk.Label(fenster, text=info_text)
    info_label.pack(pady='10')


    autorenliste = sorted(autoren_set, key=lambda x:x.name)

    #frames
    frame_links = tk.Frame(fenster)
    frame_rechts = tk.Frame(fenster)
    frame_links.pack(side='left', padx=35, pady=10)
    frame_rechts.pack(side='right', padx=35, pady=10)

    listbox_autoren = tk.Listbox(frame_links, height=100, width=30)
    for autor in autorenliste:
        listbox_autoren.insert("end",autor)
    listbox_autoren.pack()

    listbox_buecher = tk.Listbox(frame_rechts, height=100, width=60)
    listbox_buecher.pack()

    def autor_ausgewaehlt(event):
        auswahl = listbox_autoren.curselection()
        if not auswahl: return
        index = auswahl[0]
        autor_name = listbox_autoren.get(index)

        autor = autorenliste[index]
        listbox_buecher.delete(0, 'end')
        for buch in autor.buecher:
            listbox_buecher.insert('end',f'{buch.titel} - {buch.jahr}')
    listbox_autoren.bind("<ButtonRelease-1>", autor_ausgewaehlt)

# Erzeugen Sie mit tkinter ein Fenster der Größe 500×300 und dem dazugehörigen Fenstertitel.
fenster = tk.Tk()
fenster.geometry("500x300")

button = tk.Button(text="Datei öffnen", command=analysiere_datei)
button.pack(pady=10)



fenster.mainloop()
