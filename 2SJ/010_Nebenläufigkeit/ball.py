import tkinter as tk
from random import randint


class Ball(tk.Label):
    def __init__(self):
        self.bild = tk.PhotoImage(file='Bild.png')
        tk.Label.__init__(self, fenster, image=self.bild)
        self.ball_breite, self.ball_hoehe = self.bild.width(), self.bild.height()
        self.pos_x, self.pos_y = randint(0, breite - self.ball_breite), randint(0, hoehe - self.ball_hoehe)
        self.bewegung_x, self.bewegung_y = randint(1,5), randint(1,5)
        self.ball_bewegen()

    def ball_bewegen(self):
        self.pos_x += self.bewegung_x
        self.pos_y += self.bewegung_y
        if self.pos_x >= breite - self.ball_breite or self.pos_x <= 0:
            self.bewegung_x = -self.bewegung_x
        if self.pos_y > hoehe - self.ball_hoehe or self.pos_y <= 0:
            self.bewegung_y = -self.bewegung_y
        self.place(x=self.pos_x, y=self.pos_y)

        fenster.after(16, self.ball_bewegen)


fenster = tk.Tk()
breite = 800
hoehe = 800
fenster.geometry(f'{breite}x{hoehe}')
fenster.after(0, Ball) # hier erstmal nur ein Ball ;)
fenster.mainloop()