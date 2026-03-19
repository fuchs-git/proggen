import threading
import tkinter as tk
from time import sleep

def ohne_pause():
    print("Hallo")
    print("Welt")

def mit_pause():
    text = 'Warte'
    for _ in range(10):
        try:
            text += '.'
            lbl.config(text=text)
            sleep(0.5)
        except RuntimeError:
            print("Vorzeitig beendet")
            return

fenster = tk.Tk()

lbl = tk.Label(fenster, text="Hallo")
lbl.pack()

tk.Button(fenster, text="Hallo Welt", command=ohne_pause).pack(padx=80, pady=20)

tk.Button(fenster, text="Hallo - Pause - Welt", command=lambda: threading.Thread(target=mit_pause).start()).pack(padx=80, pady=20)



fenster.mainloop()