import tkinter as tk
import socket
import threading
# ---------------------------------------------------
# Verbindung zum Server herstellen
# ---------------------------------------------------
def verbinden():
    # Baut die Verbindung zum Server auf und sendet den Spielernamen.
    global name
    name = entry.get()
    sende_text("LOGIN")
    sende_text(name)
    threading.Thread(target=empfang, daemon=True).start()
# ---------------------------------------------------
# Bytes senden
# ---------------------------------------------------
def sende_bytes(data):
    # Sendet zuerst die Länge und danach die eigentlichen Daten.
    sock.sendall(len(data).to_bytes(4, "big"))
    sock.sendall(data)
# ---------------------------------------------------
# Text senden
# ---------------------------------------------------
def sende_text(text):
    # Wandelt Text in Bytes um und sendet diese.
    sende_bytes(text.encode("utf8"))
# ---------------------------------------------------
# Bytes empfangen
# ---------------------------------------------------
def empfange_bytes():
    # Empfängt zuerst die Länge und danach die Daten.
    laenge = int.from_bytes(sock.recv(4), "big")
    daten = b''
    while len(daten) < laenge:
        daten += sock.recv(laenge - len(daten))
    return daten
# ---------------------------------------------------
# Text empfangen
# ---------------------------------------------------
def empfange_text():
    # Empfängt Daten und dekodiert sie.
    return empfange_bytes().decode("utf8")
# ---------------------------------------------------
# Nachrichten empfangen
# ---------------------------------------------------
def empfang():
    # Wartet dauerhaft auf Nachrichten vom Server.
    while True:
        try:
            cmd = empfange_text()
            # Punktestand empfangen
            if cmd == "SCORE":
                neuer_score = empfange_text()
                fenster.after(0, lambda: score.config(text=neuer_score))

            # Nachricht empfangen
            elif cmd == "TEXT":
                nachricht = empfange_text()
                fenster.after(0,lambda: info.config(text=nachricht))
        except:
            break
# ---------------------------------------------------
# Treffer senden
# ---------------------------------------------------
def treffer():
    # Meldet dem Server einen Treffer.
    sende_text("TREFFER")
# ---------------------------------------------------
# Fenster
# ---------------------------------------------------
fenster = tk.Tk()
fenster.title("Moorhuhn")
fenster.geometry("800x600")
# ---------------------------------------------------
# Oberer Bereich
# ---------------------------------------------------
oben = tk.Frame(fenster)
oben.pack(pady=10)
# ---------------------------------------------------
# Eingabefeld
# ---------------------------------------------------
entry = tk.Entry(oben, width=20)
entry.pack(side="left")
# ---------------------------------------------------
# Punktestand
# ---------------------------------------------------
score = tk.Label(fenster, text="Score: 0", font=("Arial", 16))
score.pack(pady=20)
# ---------------------------------------------------
# Informationsfeld
# ---------------------------------------------------
info = tk.Label(fenster, text="Noch keine Nachricht", font=("Arial", 14))
info.pack(pady=20)
# ---------------------------------------------------
# Hauptprogramm
# ---------------------------------------------------
with socket.socket() as sock:
    # Verbindung herstellen
    sock.connect(("127.0.0.1", 12345))
    # Verbindungsbutton
    btn_verbinden = tk.Button(oben, text="Verbinden", command=verbinden)
    btn_verbinden.pack(side="left")
    # Trefferbutton
    btn_treffer = tk.Button(
        fenster,
        text="Treffer",
        width=20,
        height=5,
        command=treffer
    )
    btn_treffer.pack(pady=50)
    fenster.mainloop()