import tkinter as tk

# def funktion(event: tk.Event):
#     global inhalt
#     inhalt = entry.get()
#     label.config(text=inhalt)
#
#
# inhalt = ''
# eingabe = tk.StringVar
#
# fenster = tk.Tk()
# fenster.geometry('300x100')
# entry = tk.Entry()
# label = tk.Label()
#
# entry.pack(padx=20, pady=20)
# label.pack(padx=20, pady=2)
# entry.bind('<KeyRelease>', funktion)
# entry.bind('<KeyRelease>', lambda x: label.config(text=x.char))
#
# fenster.mainloop()


# ----------------------------------------------------------------------------------------------------------------

fenster = tk.Tk()

eingabe_var = tk.StringVar()
tk.Label(textvariable=eingabe_var).pack(padx=15, pady=5)
tk.Entry(textvariable=eingabe_var).pack(padx=15, pady=5)
tk.Button(text="Variable ausgeben", command=lambda: print(eingabe_var.get())).pack(padx=15, pady=5)
tk.Button(text="Variable löschen", command=lambda: eingabe_var.set("")).pack(padx=15, pady=5)

tk.Button(text='Inhalt ausgeben', command=lambda: print(eingabe_var.get())).pack()
tk.Button(text='Inhalt setzen', command=lambda: eingabe_var.set('HalloWelt!')).pack()

fenster.mainloop()