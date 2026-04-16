import tkinter as tk
import socket

def bewegen(e:tk.Event):
    x = e.x_root - fenster.winfo_rootx() - bild_g.width() // 2
    y = e.y_root - fenster.winfo_rooty() - bild_g.height() // 2
    kugel.place(x=x, y=y)
    print('sende gleich')
    srv.send(f'{x},{y} '.encode('utf-8'))
    print('gesendet')

fenster = tk.Tk()
fenster.title('Netzwerk Kugel')
fenster.geometry('800x600')
kugel = tk.Label(fenster, text='Kugel')


bild_r = tk.PhotoImage(file='Bild.png')
bild_g = tk.PhotoImage(file='Bild2.png')
kugel = tk.Label(fenster, image=bild_g)

srv = socket.socket()
srv.connect(('192.168.42.1', 7710))


fenster.bind("<B1-Motion>", bewegen)
fenster.mainloop()

srv.close()