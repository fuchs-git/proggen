import tkinter as tk

# ----------------- Eingabefeld -----------------
# fenster = tk.Tk()
#
# tk.Label(text="Bitte was eingeben:").pack(side=tk.LEFT, padx=25, pady=(25, 25))
# tk.Entry(width=25).pack(side=tk.RIGHT, padx=(5,20), pady=(25, 25))
#
# fenster.mainloop()


# ----------------- Eingabe ausgeben -----------------

# def btn_press():
#     s = eingabe.get()       # Entry auslesen, Wert benutzen
#     print(s)
#
# fenster = tk.Tk()
#
# tk.Label(text="ein Eingabefeld").pack(padx=25, pady=(25, 5))
# eingabe = tk.Entry(width=25)
# eingabe.pack(padx=25, pady=5)
#
# tk.Button(text="jetzt die Eingabe auslesen", command=btn_press).pack(padx=25, pady=(5, 25))
# # Konsolen-Output beachten!
#
# fenster.mainloop()

# ----------------- Eingabe löschen -----------------

def btn_loeschen_alles():
    eingabe.delete(0, tk.END)
    # zwei Parameter, erster Index inklusive,
    # zweiter Index Exklusive oder tk.END für "bis zum Ende"

def btn_loeschen_vorn():
    eingabe.delete(0)
    # ein Parameter => dieses Zeichen löschen

def btn_loeschen_hinten():
    eingabe.delete(len(eingabe.get()) - 1)
    # das letzte Zeichen hat den Index "Länge minus 1"
    # (wie in jedem anderen String auch)

def btn_auslesen():
    wert = eingabe.get()
    lbl_ausgabe_wert.configure(text=wert)
    print(wert)

fenster = tk.Tk()

frm_links = tk.Frame()  # linke Spalte
frm_rechts = tk.Frame()  # rechte Spalte

frm_links.pack(side=tk.LEFT)
frm_rechts.pack(side=tk.LEFT)

tk.Label(frm_links, text='Eingabe:', ).pack()
tk.Button(frm_links, text='auslesen', command=btn_auslesen).pack()
tk.Button(frm_links, text='alles löschen', command=btn_loeschen_alles).pack()
lbl_ausgabe_lbl = tk.Label(frm_links, text="Ausgabe:")
lbl_ausgabe_lbl.pack()

eingabe = tk.Entry(frm_rechts, width=25)
eingabe.pack()
tk.Button(frm_rechts, text='erstes Zeichen löschen', command=btn_loeschen_vorn).pack()
tk.Button(frm_rechts, text='letztes Zeichen löschen', command=btn_loeschen_hinten).pack()
lbl_ausgabe_wert = tk.Label(frm_rechts)
lbl_ausgabe_wert.pack()

fenster.mainloop()