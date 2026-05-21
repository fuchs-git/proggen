import tkinter as tk
import socket
import threading


class Client(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        self.geometry("800x600")

        self.sock = socket.socket()

        self.bild = None
        self.bild_id = None

        self.gui()

    def gui(self):
        oben = tk.Frame(self)
        oben.pack()

        self.entry = tk.Entry(oben)
        self.entry.pack(side="left")

        tk.Button(oben, text="Verbinden", command=self.verbinden).pack(side="left")

        self.score = tk.Label(self, text="")
        self.score.pack()

        self.canvas = tk.Canvas(self, width=700, height=500, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.klick)

    def sende_bytes(self, data):
        self.sock.sendall(len(data).to_bytes(4, "big"))
        self.sock.sendall(data)

    def sende_text(self, text):
        self.sende_bytes(text.encode("utf8"))

    def empfange_bytes(self):
        laenge = int.from_bytes(self.sock.recv(4), "big")

        daten = b''
        while len(daten) < laenge:
            daten += self.sock.recv(laenge - len(daten))

        return daten

    def empfange_text(self):
        return self.empfange_bytes().decode("utf8")

    def verbinden(self):
        self.sock.connect(("127.0.0.1", 12346))

        self.name = self.entry.get()

        self.sende_text("LOGIN")
        self.sende_text(self.name)

        threading.Thread(target=self.empfang, daemon=True).start()

    def empfang(self):
        while True:
            try:
                cmd = self.empfange_text()

                if cmd == "BILD":
                    dateiname = self.empfange_text()
                    data = self.empfange_bytes()

                    self.after(0, lambda: self.zeige_bild(data))

                elif cmd == "POS":
                    pos = self.empfange_text()
                    x, y = map(int, pos.split(";"))

                    self.after(0, lambda: self.canvas.coords(self.bild_id, x, y))

                elif cmd == "SCORE":
                    score = self.empfange_text()

                    self.after(0, lambda: self.score.config(text=score))

            except:
                break

    def zeige_bild(self, data):
        self.bild = tk.PhotoImage(data=data)

        self.bild_id = self.canvas.create_image(
            100, 100,
            image=self.bild,
            anchor="nw"
        )

    def klick(self, event):
        if self.bild_id is None:
            return

        x1, y1 = self.canvas.coords(self.bild_id)

        x2 = x1 + self.bild.width()
        y2 = y1 + self.bild.height()

        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            self.sende_text("TREFFER")


app = Client()
app.mainloop()