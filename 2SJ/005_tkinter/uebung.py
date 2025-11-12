import tkinter as tk
import tk_db


def addieren():
    anzahl.set(db.read() +1)
    wert =int(anzahl.get())
    db.speichern(wert)

db = tk_db.Datenbank()
# db.createDB()
# db.createTbl()


fenster = tk.Tk()

anzahl = tk.IntVar(value=db.read())
lbl = tk.Label(textvariable=anzahl)
lbl.pack()
btn = tk.Button(text='push', command=addieren)
btn.pack()

fenster.mainloop()
