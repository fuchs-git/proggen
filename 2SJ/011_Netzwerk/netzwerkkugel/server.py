import tkinter as tk
import socket
import threading

def funktion():
    nachricht = ''
    with socket.socket() as server_socket:
        server_socket.bind(('', 7710))
        server_socket.listen()
        client, info = server_socket.accept()
        kugel.config(image=bild_g)
    while True:
        nachricht += client.recv(12).decode('utf-8')
        print(nachricht)
        if ' ' in nachricht:
            geteilt = nachricht.split(',',maxsplit=1)
            if len(geteilt) == 2:
                koord, nachricht = geteilt
            else:
                koord, nachricht = geteilt[0], ''
            x,y = koord.split(',')
            kugel.place(x=x, y=y)


threading.Thread(target=funktion).start()

fenster = tk.Tk()
fenster.title('Netzwerk Kugel - Server')
fenster.geometry('800x600')
kugel = tk.Label(fenster, text='Kugel')


bild_r = tk.PhotoImage(file='Bild.png')
bild_g = tk.PhotoImage(file='Bild2.png')
kugel = tk.Label(fenster, image=bild_r)

# fenster.bind("<B1-Motion>", bewegen)

fenster.mainloop()
