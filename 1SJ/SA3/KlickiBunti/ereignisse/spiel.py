import tkinter as tk
import random

def maus_auf_knopf(event):
    phrasen = ['keine Chance', 'niemals', 'mich fängt niemand', 'keiner kriegt mich', 'nie im Leben', 'no way',
               'unmöglich', 'gib auf', 'im Leben nicht', 'bleib mir vom Leib', 'ich bin zu schnell', 'du bist zu langsam']

    btn.configure(text=random.choice(phrasen))  # eine Option neu festlegen

    btn_x = btn_neu_x = btn.winfo_x()  # Knopf-Position in mehrere Variablen gleichzeitig
    btn_y = btn_neu_y = btn.winfo_y()  #
    maus_x = btn_x + event.x  # Mausposition relativ zum Fenster
    maus_y = btn_y + event.y

    btn_w = btn.winfo_width()  # Knopf-Größe
    btn_h = btn.winfo_height()

    # solange die Maus über dem Knopf wäre,
    # verschiebe die Knopf-Koordinaten zufällig
    while ((btn_neu_x <= maus_x < btn_neu_x + btn_w)
           and
           (btn_neu_y <= maus_y < btn_neu_y + btn_h)):
        btn_neu_x = random.randint(0, fenster.winfo_width() - btn_w - 20)
        btn_neu_y = random.randint(0, fenster.winfo_height() - btn_h - 20)

    # setze den Knopf an die neuen Koordinaten
    btn.place(x=btn_neu_x, y=btn_neu_y)

fenster = tk.Tk()
fenster.minsize(600, 400)  # :-)

btn = tk.Button(text='klick mich', command=lambda: print('Du bist ein Weiser auf dem Weg zur Erleuchtung!'))
btn.bind('<Enter>', maus_auf_knopf)
btn.pack(pady=10)

fenster.mainloop()