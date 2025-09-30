import tkinter as tk
from tkinter import filedialog


def analysiere_datei():
    global autoren_dict, links, rechts
    filename = filedialog.askopenfilename(
        filetypes=[("Text-Dateien", "*.csv")],
        title="Wähle eine CSV-Datei aus",
    )
    with open(filename, 'r') as f:
        f.readline()
        books = f.read().splitlines()

    for book in books:
        id, autor, titel, jahr = book.split(';')
        if autor not in autoren_dict:
            autoren_dict[autor] = []
        autoren_dict[autor].append(f'{titel} ({jahr})')

    # stats
    anzahl_autoren = len(autoren_dict)
    anzahl_buecher = sum([len(i) for _, i in autoren_dict.items()])

    tk.Label(text=f'Anzahl Autoren: {anzahl_autoren}, insgesamte Bücher: {anzahl_buecher}.').pack(pady=10)

    # ListBoxen
    links = tk.Listbox(fenster)
    rechts = tk.Listbox(fenster)
    links.pack(side='left', expand=True, fill='both')
    rechts.pack(side='right', expand=True, fill='both')

    for autor in sorted(autoren_dict):
        links.insert('end', autor)

    links.bind('<ButtonRelease-1>', ausgewaehlt)


def ausgewaehlt(event):
    global autoren_dict
    rechts.delete(0, 'end')
    auswahl = links.curselection()
    index = auswahl[0]
    autor = links.get(index)
    print(autor)

    for a, books in autoren_dict.items():
        for book in books:
            if a == autor:
                rechts.insert('end', book)


autoren_dict = {}
links = None
rechts = None

fenster = tk.Tk()
fenster.geometry('800x400')
fenster.title('Autoren und Buecher')

btn = tk.Button(text='Datei öffnen', command=analysiere_datei)
btn.pack(pady=10)

fenster.mainloop()
