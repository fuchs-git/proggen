import tkinter as tk

# (lambda :print("hallo"))()

liste = ["ab", "b", "7xxx"]
print(sorted(liste, key=lambda x: len(x), reverse=True))


def sag_etwas(etwas):
    print(etwas)


fenster = tk.Tk()
# fenster.geometry("+2800+300")
# tk.Button(text="sag hallo", command=lambda: print("Hallo"), padx=20, pady=20).pack(padx=30, pady=30)
tk.Button(text="sag hallo", command=lambda: sag_etwas("hallo"), padx=20, pady=20).pack(padx=30, pady=30)
tk.Button(text="sag hallo", command=lambda: sag_etwas("welt"), padx=20, pady=20).pack(padx=30, pady=30)
fenster.mainloop()



def hallo():
    print(x)
    x=1
hallo()