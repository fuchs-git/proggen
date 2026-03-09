import tkinter as tk
from time import sleep

def ohne_pause():
    print("Hallo")
    print("Welt")

def mit_pause():
    print("Hallo")
    sleep(3)
    print("Welt")

fenster = tk.Tk()

tk.Button(fenster, text="Hallo Welt", command=ohne_pause).pack(padx=80, pady=20)

tk.Button(fenster, text="Hallo - Pause - Welt", command=mit_pause).pack(padx=80, pady=20)

fenster.mainloop()