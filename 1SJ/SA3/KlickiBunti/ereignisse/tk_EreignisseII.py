import tkinter as tk


# ----------------- Mausposition -----------------
# def callback(event:tk.Event):
#     print(f'Klick bei x={event.x}, y={event.y}')
#
# fenster = tk.Tk()
# fenster.geometry('500x400')
#
# fenster.bind('<ButtonPress-1>', callback)
# oder fenster.bind('<1>', callback) oder fenster.bind('<1>', callback)
#
# fenster.mainloop()

# ----------------- Maustasten -----------------
# fenster = tk.Tk()
# fenster.geometry('500x400')
#
# fenster.bind('<ButtonPress-1>', lambda maus: print('links', maus.x, maus.y))
# fenster.bind('<Button-2>', lambda maus: print('mitte', maus.x, maus.y))
# fenster.bind('<3>', lambda maus: print('rechts', maus.x, maus.y))
#
# fenster.mainloop()

# ----------------- Maustasten im Widget -----------------
# fenster = tk.Tk()
# fenster.geometry('500x400')
#
# lbl_a = tk.Label(text='Label A', bg='orange', width=30, height=3)
# lbl_a.pack()
#
# lbl_b = tk.Label(text='Label B', bg='green', width=30, height=3)
# lbl_b.pack(expand=True, fill=tk.X)
#
# lbl_a.bind('<Button-1>', lambda maus: print(maus.x, maus.y))
# lbl_b.bind('<Button-1>', lambda maus: print(maus.x, maus.y))
#
# fenster.mainloop()

# ----------------- Koordinaten -----------------
# fenster = tk.Tk()
# fenster.geometry('500x400')
#
# lbl = [tk.Label(text=f'Lbl{i}: niemand hat mich geklickt', bg='orange', width=50, height=3) for i in range(6)]
# for l in lbl:
#     l.pack(padx=5, pady=5)
#     l.bind('<Button-1>', lambda maus: print(f'relativ zum Widget: {maus.x} {maus.y}'))
#     l.bind('<Button-2>', lambda maus: print(f'relativ zum Bildschirm: {maus.x_root} {maus.y_root}'))
#     l.bind('<Button-3>', lambda maus: print(f'relativ zum Fenster: {maus.widget.winfo_x() + maus.x}, {maus.widget.winfo_y() + maus.y}'))
#
# fenster.mainloop()

# ----------------- Rein & Raus -----------------
# fenster = tk.Tk()
# fenster.geometry('500x400')
#
# btn = tk.Button(text='KlickMe', command=lambda: print('es wurde geklickt'))
# btn.pack(padx=20, pady=10)
#
# btn.bind('<Enter>', lambda x: print('rein'))
# btn.bind('<Leave>', lambda x: print('raus'))
#
# fenster.mainloop()

# ----------------- Rein & Raus & Koordinaten -----------------
# def rein(event):
#     print('Einige aktuelle Koordinaten:')
#     print(f'\tKnopf (x,y)-Position: ({btn.winfo_x()},{btn.winfo_y()})')
#     print(f'\tKnopf (Breite,Höhe): {btn.winfo_width()},{btn.winfo_height()})')
#     print(f'\tMaus (x,y)-Position (relativ zum Knopf): {event.x},{event.y=})')
#     print(f'\tMaus (x,y)-Position (relativ zum Fenster): {event.x+btn.winfo_x()},{event.y+btn.winfo_y()})')
#     print(f'\tFenster (x,y)-Position: {fenster.winfo_x()},{fenster.winfo_y()})')
#     print(f'\tFenster (Breite,Höhe): {fenster.winfo_width()},{fenster.winfo_height()})')
#
# fenster = tk.Tk()
#
# fenster.minsize(500, 400)
#
# btn = tk.Button(text='klick mich', command=lambda: print('es wurde geklickt'))
# btn.pack()
#
# btn.bind('<Enter>', rein)
#
# fenster.mainloop()
