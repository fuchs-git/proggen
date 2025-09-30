import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Autor:
    def __init__(self, name: str):
        self.name = name
        self.buecher = set()

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return isinstance(other, Autor) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


class Buch:
    def __init__(self, ID: str, Titel: str, Jahr: str, autor: Autor):
        self.id = ID
        self.titel = Titel
        self.jahr = Jahr
        self.autor = autor

    def __repr__(self):
        return f'{self.titel} ({self.jahr})'

    def __eq__(self, other):
        return isinstance(other, Buch) and self.titel == other.titel and self.autor == other.autor

    def __hash__(self):
        return hash((self.titel, self.autor))


def analysiere_datei():
    filename = filedialog.askopenfilename(
        filetypes=[("CSV-Dateien", "*.csv")],
        title="Wähle eine CSV-Datei aus"
    )

    if not filename:
        return  # Dialog abgebrochen

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            next(f)  # Kopfzeile überspringen

            autoren_set = set()
            buecher_liste = []

            for line in f:
                if line.strip() == '':
                    continue
                id_, autor_name, titel, jahr = line.strip().split(';')

                autor = Autor(autor_name)
                if autor not in autoren_set:
                    autoren_set.add(autor)
                else:
                    for a in autoren_set:
                        if a.name == autor_name:
                            autor = a
                            break

                buch = Buch(id_, titel, jahr, autor)
                autor.buecher.add(buch)
                buecher_liste.append(buch)

    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Öffnen der Datei:\n{e}")
        return

    zeige_statistik(autoren_set, buecher_liste)


def zeige_statistik(autoren, buecher):
    label_info.config(text=f"{len(autoren)} Autoren, {len(buecher)} Bücher, {len(set(buecher))} unterschiedliche Bücher")

    listbox_autoren.delete(0, tk.END)
    for autor in sorted(autoren, key=lambda a: a.name):
        listbox_autoren.insert(tk.END, autor.name)

    global autoren_liste
    autoren_liste = list(sorted(autoren, key=lambda a: a.name))


def autor_ausgewaehlt(event):
    selection = listbox_autoren.curselection()
    if not selection:
        return
    index = selection[0]
    autor = autoren_liste[index]

    listbox_buecher.delete(0, tk.END)
    for buch in sorted(autor.buecher, key=lambda b: b.titel):
        listbox_buecher.insert(tk.END, repr(buch))


# GUI Setup
fenster = tk.Tk()
fenster.geometry('500x300')
fenster.title("Bibliotheksanalyse")

btn = tk.Button(fenster, text='Datei öffnen', command=analysiere_datei)
btn.pack(pady=5)

label_info = tk.Label(fenster, text="Keine Datei geladen")
label_info.pack()

frame = tk.Frame(fenster)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

frame_links = tk.Frame(frame)
frame_links.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

frame_rechts = tk.Frame(frame)
frame_rechts.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

tk.Label(frame_links, text="Autoren").pack()
listbox_autoren = tk.Listbox(frame_links)
listbox_autoren.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_rechts, text="Bücher").pack()
listbox_buecher = tk.Listbox(frame_rechts)
listbox_buecher.pack(fill=tk.BOTH, expand=True)

listbox_autoren.bind('<<ListboxSelect>>', autor_ausgewaehlt)

autoren_liste = []

fenster.mainloop()
