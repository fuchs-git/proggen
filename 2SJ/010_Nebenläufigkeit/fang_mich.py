import tkinter as tk
import random


def gefangen():
    global soll_sich_bewegen
    soll_sich_bewegen = not soll_sich_bewegen
    print('erwischt')
    if soll_sich_bewegen:
        btn_bewegen()

def btn_bewegen():
    global x, bx, y, by

    x += bx
    y += by

    if x <0:
        bx = random.randint(10,50)
        # bx = -bx
        x = -x
    elif x>fenster.winfo_width()-btn.winfo_width():
        bx = -bx
        x = fenster.winfo_width()-btn.winfo_width()

    if y <0:
        by = random.randint(10,50)
        y = -y
    elif y>fenster.winfo_height()-btn.winfo_height():
        by = -by
        y = fenster.winfo_height()-btn.winfo_height()


    btn.place(x=x, y=y)

    if soll_sich_bewegen: fenster.after(50, btn_bewegen)

fenster = tk.Tk()
fenster.geometry(f'800x800')

soll_sich_bewegen = False
x = 700
y = 700

bx = 3
by = 3

btn = tk.Button(fenster, text='fang mich', height=4, command=gefangen)
btn.place(x=x, y=100)
btn_bewegen()


fenster.mainloop()
