# import tkinter as tk
#
# def callback(event):
#     print(f"Klick bei x={event.x}, y={event.y}")
#
# fenster = tk.Tk()
# fenster.geometry("500x400")
#
# fenster.bind("<ButtonPress-1>", callback)
# # ------^^^^------
# fenster.mainloop()


# # Mauszeiger
# import tkinter as tk
#
#
# def maus_links(event):
#     print("links", event.x, event.y)
#
#
# def maus_mitte(event):
#     print("mitte", event.x, event.y)
#
#
# def maus_rechts(event):
#     print("rechts", event.x, event.y)
#
#
# fenster = tk.Tk()
# fenster.geometry("500x400")
#
#
# # fenster.bind("<ButtonPress-1>", maus_links)
# # fenster.bind("<Button-2>", maus_mitte)
# fenster.bind("<1>", maus_links)
# fenster.bind("<2>", maus_mitte)
# fenster.bind("<3>", maus_rechts)
#
# fenster.mainloop()


import tkinter as tk


def maustaste(event):
    print(f"\nKoordinaten relativ zum Widget: {event.x}, {event.y}")
    print(f"Koordinaten relativ zum Bildschirm: {event.x_root}, {event.y_root}")
    print(f"Koordinaten relativ zum Fenster: {event.widget.winfo_x() + event.x}, {event.widget.winfo_y() + event.y}")

    taste = ['nix', 'links', 'mitte', 'rechts'][event.num]  # die Maustasten sind ja 1, 2 und 3
    farbe = ['orange', 'lightgreen', 'crimson', 'blue'][event.num]
    event.widget.configure(text="ich wurde mit " + taste + " angeklickt", bg=farbe)
    print(taste)


fenster = tk.Tk()
fenster.geometry("500x400")

labels = [tk.Label(text="niemand hat mich angeklickt", bg='orange', width=50, height=3) for _ in range(6)]
for lbl in labels:
    lbl.pack(padx=5, pady=5)
    lbl.bind("<ButtonPress-1>", maustaste)
    lbl.bind("<Button-2>", maustaste)
    lbl.bind("<3>", maustaste)

fenster.mainloop()