import tkinter as tk
import socket
import base64

def anzeigen():
    text = eingabe.get()

    with socket.socket() as bild:
        bild.connect(('192.168.42.6', 7710))
        bild.send(text.encode('utf-8'))

        data = b''
        while True:
            chunk = bild.recv(4096)
            if not chunk:
                break
            data += chunk

    b64_data = base64.b64encode(data).decode('ascii')
    photo = tk.PhotoImage(data=b64_data)

    lbl2.config(image=photo)
    lbl2.image = photo

fenster = tk.Tk()
fenster.title('Bildipedia Kugel')
fenster.geometry('900x600')

lbl = tk.Label(fenster, text='Was für ein Bild soll angezeigt werden?')
lbl.pack()

eingabe = tk.Entry(fenster)
eingabe.pack()

tk.Button(fenster, text='Suchen', command=anzeigen).pack()

lbl2 = tk.Label(fenster)
lbl2.pack()

fenster.mainloop()