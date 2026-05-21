import socket
import threading
import random
import time


class Server:

    def __init__(self):
        self.clients = []
        self.spieler = {}
        self.lock = threading.Lock()

    def sende_bytes(self, data, client):
        client.sendall(len(data).to_bytes(4, "big"))
        client.sendall(data)

    def sende_text(self, text, client):
        self.sende_bytes(text.encode("utf8"), client)

    def empfange_bytes(self, client):
        laenge = int.from_bytes(client.recv(4), "big")

        daten = b''
        while len(daten) < laenge:
            daten += client.recv(laenge - len(daten))

        return daten

    def empfange_text(self, client):
        return self.empfange_bytes(client).decode("utf8")

    def sende_score(self):
        score = ";".join(f"{name}:{punkte}" for name, punkte in self.spieler.items())

        for c in self.clients:
            try:
                self.sende_text("SCORE", c)
                self.sende_text(score, c)
            except:
                pass

    def sende_position(self):
        x = random.randint(50, 600)
        y = random.randint(50, 400)

        for c in self.clients:
            try:
                self.sende_text("POS", c)
                self.sende_text(f"{x};{y}", c)
            except:
                pass

    def sende_bild(self, client):
        with open("moorhuhn.png", "rb") as f:
            data = f.read()

        self.sende_text("BILD", client)
        self.sende_text("moorhuhn.png", client)
        self.sende_bytes(data, client)

    def bewegung(self):
        while True:
            self.sende_position()
            time.sleep(2)

    def client_thread(self, client):
        name = ""

        try:
            while True:
                cmd = self.empfange_text(client)

                if cmd == "LOGIN":
                    name = self.empfange_text(client)

                    with self.lock:
                        self.spieler[name] = 0

                    self.sende_bild(client)
                    self.sende_score()

                elif cmd == "TREFFER":
                    with self.lock:
                        self.spieler[name] += 1

                    self.sende_score()

        except:
            pass

        finally:
            if client in self.clients:
                self.clients.remove(client)

            if name in self.spieler:
                del self.spieler[name]

            client.close()

    def start(self):
        threading.Thread(target=self.bewegung, daemon=True).start()

        with socket.socket() as srv:
            srv.bind(("", 12346))
            srv.listen()

            while True:
                client, _ = srv.accept()

                self.clients.append(client)

                threading.Thread(
                    target=self.client_thread,
                    args=(client,),
                    daemon=True
                ).start()


Server().start()