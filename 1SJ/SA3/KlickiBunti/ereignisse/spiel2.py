import tkinter as tk
import random


def maus_auf_knopf(event, btn):
    phrasen = ['keine Chance', 'niemals', 'mich fängt niemand', 'keiner kriegt mich', 'nie im Leben', 'no way',
               'unmöglich', 'gib auf', 'im Leben nicht', 'bleib mir vom Leib', 'ich bin zu schnell',
               'du bist zu langsam']

    btn.configure(text=random.choice(phrasen))

    btn_x = btn_neu_x = btn.winfo_x()
    btn_y = btn_neu_y = btn.winfo_y()
    maus_x = btn_x + event.x
    maus_y = btn_y + event.y

    btn_w = btn.winfo_width()
    btn_h = btn.winfo_height()

    while ((btn_neu_x <= maus_x < btn_neu_x + btn_w)
           and (btn_neu_y <= maus_y < btn_neu_y + btn_h)):
        btn_neu_x = random.randint(0, fenster.winfo_width() - btn_w - 20)
        btn_neu_y = random.randint(0, fenster.winfo_height() - btn_h - 20)

    btn.place(x=btn_neu_x, y=btn_neu_y)


fenster = tk.Tk()
fenster.minsize(800, 600)
fenster.title("100 Unklickbare Buttons")

buttons = []

for _ in range(1000):
    btn = tk.Button(fenster, text='Klick mich', command=lambda: print('Erwischt!'))
    btn.bind('<Enter>', lambda event, b=btn: maus_auf_knopf(event, b))
    btn.place(x=random.randint(0, 750), y=random.randint(0, 550))
    buttons.append(btn)

fenster.mainloop()