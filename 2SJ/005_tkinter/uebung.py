import tkinter as tk
import tk_db


def setup():
    db.createDB()
    db.createTbl()


def addieren():
    anzahl.set(db.read() + 1)
    wert = int(anzahl.get())
    db.speichern(wert)


db = tk_db.Datenbank()
fenster = tk.Tk()
fenster.geometry('180x80')

anzahl = tk.IntVar(value=db.read())
lbl = tk.Label(textvariable=anzahl)
lbl.pack()
btn = tk.Button(text='push', command=addieren)
btn.pack()

fenster.mainloop()
