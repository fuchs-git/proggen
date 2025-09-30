import tkinter as tk


class TicTacToe():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.wahl = "X"
        self.frame1 = tk.Frame(master=self.root, bg="red")
        self.frame2 = tk.Frame(master=self.root, bg="green")
        self.frame3 = tk.Frame(master=self.root, bg="blue")
        self.label = tk.Label(master=self.root, text=self.wahl)

        self.frame1.pack(fill=tk.BOTH, expand=True)
        self.frame2.pack(fill=tk.BOTH, expand=True)
        self.frame3.pack(fill=tk.BOTH, expand=True)
        self.label.pack(fill=tk.BOTH, expand=True)
        self.btns = []
        for i in range(1, 10):
            if i <= 3:
                self.btn = tk.Button(master=self.frame1, text=" ", font="Monospace",
                                     command=lambda x=i: self.anzeige(x))
                self.btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            if i > 3 and i <= 6:
                self.btn = tk.Button(master=self.frame2, text=" ", font="Monospace",
                                     command=lambda x=i: self.anzeige(x))
                self.btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            if i > 6:
                self.btn = tk.Button(master=self.frame3, text=" ", font="Monospace",
                                     command=lambda x=i: self.anzeige(x))
                self.btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.btns.append(self.btn)

        # self.btn2 = tk.Button(master=self.frame1)
        # self.btn3 = tk.Button(master=self.frame1)
        # self.btn4 = tk.Button(master=self.frame2)
        # self.btn5 = tk.Button(master=self.frame2)
        # self.btn6 = tk.Button(master=self.frame2)
        # self.btn7 = tk.Button(master=self.frame3)
        # self.btn8 = tk.Button(master=self.frame3)
        # self.btn9 = tk.Button(master=self.frame3)

        self.root.mainloop()

    def anzeige(self, btnnr: int):
        self.btnnr = btnnr
        # self.buttons = 1

        if self.wahl == "X":
            self.wahl = "O"
            self.btns[btnnr - 1].config(text="X")
            self.label.config(text=self.wahl)
            return "X"
        if self.wahl == "O":
            self.wahl = "X"
            self.btns[btnnr - 1].config(text="O")
            self.label.config(text=self.wahl)
            return "O"


TicTacToe()
