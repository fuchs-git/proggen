import time, platform, tkinter as tk, multiprocessing as mp

STEPS = 100  # 30-10000, größer → genauere Aussage → schönere Grafik, mehr Rechenzeit
STEPS = (STEPS // 2) * 2  # muss gerade sein

# # Schwarz-Rot|Schwarz nicht-linear
# FARBEN = [f'#{int(255 * ((i / STEPS) ** .5)):02x}0000' for i in range(STEPS)] + ['#000000']

# Schwarz-Rot-Gelb|Schwarz nicht-linear
FARBEN = ([f'#{int(255 * ((i / (STEPS // 2)) ** .5)):02x}0000' for i in range(STEPS // 2)] +
          [f'#FF{int(255 * ((i / (STEPS // 2)) ** .25)):02x}00' for i in range(STEPS // 2)] +
          ['#000000'])

X, Y = 1024, 768  # Bild-Abmessungen in Pixel
ZEILEN_BLOCK = 10  # wieviele Pixel-Zeilen am Stück berechnet werden, sollte die Höhe glatt teilen
ZOOM_FACTOR = .4  # wieviel Prozent beim scrollenb hinein-/heraus-gezoomt wird, .4==40%

OS = platform.system()  # Linux/Windows/MacOS

def male(image: tk.PhotoImage,
         color: str,  # color=' #00x00x00x' RGB in HEX
         pos: tuple = None  # pos=(x,y), None bedeutet (0,0)
         ):  # je nach Anzahl dieser Farb-Strings sind das ein oder mehr Pixel
    image.put(color, pos)

def mandelbrot(c: complex):
    """
    Prüft ob eine (komplexe) Zahl teil der Mandelbrotmenge ist
    https://de.wikipedia.org/wiki/Mandelbrot-Menge
    :param c: eine komplexe Zahl
    :return: Anzahl der Iterationen bis zum Scheitern oder STEPS, wenn die Zahl nicht gescheitert ist
    """
    z = c
    for i in range(STEPS):
        a = z * z
        z = a + c
        if a.real >= 4.:
            return i  # c gehört nicht dazu
    return STEPS  # c gehört vielleicht dazu

def rechne_n_zeilen(args):
    zeile_0, xp, yp, xd, yd = args
    return " ".join("{"  # Zeilenanfang
                    + " ".join(FARBEN[mandelbrot(complex(xp + xd * spalte / X,
                                                         yp + yd * (zeile_0 + zeile_i) / Y))]
                               for spalte in range(X))  # Zeile
                    + "}"  # Zeilenende
                    for zeile_i in range(ZEILEN_BLOCK))  # mehrere Zeilen

def rechne_bild():
    print((xp, yp), (xd, yd))  # Rechteck: (x,y), (breite, höhe)
    widgets = (canvas, btn_start, btn_reset, cb, btn_exit, lbl_hilfe)
    for w in widgets:
        w.configure(state=tk.DISABLED)

    lbl_status.configure(text='berechne...')
    fenster.update()  # Anzeige erzwingen

    start = time.time()
    if use_mp.get():  # mit MP
        zeilen = pool.map(rechne_n_zeilen, [(zeile, xp, yp, xd, yd) for zeile in range(0, Y, ZEILEN_BLOCK)])
        lbl_status.configure(text=f"berechnet in {time.time() - start:.3f} Sekunden ({mp.cpu_count()} Kerne)")
    else:  # ohne MP
        zeilen = list(map(rechne_n_zeilen, [(zeile, xp, yp, xd, yd) for zeile in range(0, Y, ZEILEN_BLOCK)]))
        lbl_status.configure(text=f"berechnet in {time.time() - start:.3f} Sekunden (1 Kern)")
    male(img, ' '.join(zeilen))

    for w in widgets:
        w.configure(state=tk.NORMAL)

def dragstart(e: tk.Event):
    canvas._x_alt = e.x
    canvas._y_alt = e.y

def dragstop(e: tk.Event):
    global xp, yp
    x_move = (canvas._x_alt - e.x) * xd / X
    y_move = (canvas._y_alt - e.y) * yd / Y
    xp, yp = xp + x_move, yp + y_move
    rechne_bild()

def scroll(event: tk.Event):
    if canvas.cget('state') != tk.DISABLED:
        global xp, yp, xd, yd
        match OS:
            case 'Linux':
                match event.num:
                    case 4:
                        wert = -1
                    case 5:
                        wert = 1
            case 'Windows':
                wert = -int((event.delta / 120))
            case 'Darwin':  # MacOS
                wert = -event.delta
            case _:  # unbekanntes OS
                wert = event.delta  # (kA)

        if wert > 0:  # raus: Position behalten, nur zoomen
            xm, ym = xp + xd / 2, yp + yd / 2
            zf = 1 + ZOOM_FACTOR
        else:  # rein: Position zur Maus schieben, zoomen
            xm, ym = xp + xd * event.x / X, yp + yd * event.y / Y
            zf = 1 - ZOOM_FACTOR
        xd, yd = xd * zf, yd * zf
        xp, yp = xm - xd / 2, ym - yd / 2

        rechne_bild()

def reset():
    global xp, yp, xd, yd
    xp, yp = -2.0, -1.27  # Koordinaten des Bildausschnitts (links oben)...
    xd, yd = 3.0, 2.54  # Breite, Höhe
    rechne_bild()

if __name__ == "__main__":
    fenster = tk.Tk()

    img = tk.PhotoImage(width=X, height=Y)
    canvas = tk.Canvas(master=fenster, width=X, height=Y, bg="#000000");
    canvas.pack()
    canvas.create_image((0, 0), image=img, state="normal", anchor=tk.NW)
    if OS == "Linux":
        canvas.bind('<4>', scroll)
        canvas.bind('<5>', scroll)
    else:  # Windows + MacOS (+ andere ???)
        canvas.bind("<MouseWheel>", scroll)
    canvas.bind('<ButtonPress-1>', dragstart)
    canvas.bind('<ButtonRelease-1>', dragstop)

    lbl_status = tk.Label(fenster, text='noch nicht berechnet')
    lbl_status.pack()

    use_mp = tk.BooleanVar()
    use_mp.set(True)  # True -> mp initial ein; False, mp initial aus
    cb = tk.Checkbutton(master=fenster, text="multiprocessing",
                        variable=use_mp, onvalue=True, offvalue=False)
    cb.pack(side=tk.LEFT, padx=10, pady=10)

    btn_start = tk.Button(text="Neu berechnen", command=rechne_bild)
    btn_start.pack(side=tk.LEFT, padx=10, pady=10)
    btn_reset = tk.Button(text="Reset", command=reset)
    btn_reset.pack(side=tk.LEFT, padx=10, pady=10)
    lbl_hilfe=tk.Label(fenster, text="scrollen zum zoomen, drag&drop zum verschieben")
    lbl_hilfe.pack(side=tk.LEFT, padx=10, pady=10)
    btn_exit = tk.Button(text="Beenden", command=exit)
    btn_exit.pack(side=tk.RIGHT, padx=10, pady=10)

    xp = yp = xd = yd = None
    pool = mp.Pool()
    reset()

    fenster.mainloop()

    pool.close()
    pool.join()