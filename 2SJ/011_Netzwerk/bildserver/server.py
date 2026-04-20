import socket
import threading

def funktion():
    bilder = {
        "katze": "Katze.png",
        "tiger": "Tiger.png",
        "nackmull": "nackmull.png"
    }

    with socket.socket() as server_socket:
        server_socket.bind(('', 7710))
        server_socket.listen()

        while True:
            client, addr = server_socket.accept()
            print(f"Verbunden mit {addr}")

            with client:
                nachricht = client.recv(1024).decode('utf-8').lower()
                print("Empfangen:", nachricht)

                for keyword, datei in bilder.items():
                    if keyword in nachricht:
                        try:
                            with open(datei, 'rb') as img:
                                daten = img.read()
                                client.sendall(daten)
                                print(f"{datei} gesendet")
                        except FileNotFoundError:
                            print(f"Datei {datei} nicht gefunden")
                        break
                else:
                    with open('nackmull.png', 'rb') as img:
                        daten = img.read()
                        client.sendall(daten)
                        print(f"Datei {keyword} nicht gefunden")

threading.Thread(target=funktion, daemon=True).start()

input("Server läuft...")