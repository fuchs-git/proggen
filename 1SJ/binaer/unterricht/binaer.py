import tkinter as tk
from zipfile import crc32

with open('proggen.bmp', 'rb') as f:
    magic_code = bytearray(f.read(2))
    if magic_code == b'BM':
        groesse = int.from_bytes(f.read(4), byteorder='little')
        # print('Größe',256 ** 0 * groesse[0] +
        #       256 ** 1 * groesse[1] +
        #       256 ** 2 * groesse[2] +
        #       256 ** 3 * groesse[3])
        print(f'{groesse=}')
        f.read(4) # reserviert
        offset = int.from_bytes(f.read(4), byteorder='little')
        print(f'{offset=}')

        # ab hier Info-Block (40 Byte)
        groesse_infoheader = int.from_bytes(f.read(4), byteorder='little')
        print(f'{groesse_infoheader=}')

        breite_bitmap = int.from_bytes(f.read(4), byteorder='little', signed=True)
        print(f'{breite_bitmap=}')

        hoehe_bitmap = int.from_bytes(f.read(4), byteorder='little', signed=True)
        print(f'{hoehe_bitmap=}')

        if hoehe_bitmap <0:
            hoehe_bitmap =-hoehe_bitmap
            bild_bottum_up = False
        else:
            bild_bottum_up = True

        farbebene = int.from_bytes(f.read(2), byteorder='little')
        print(f'{farbebene=}')

        farbtiefe = int.from_bytes(f.read(2), byteorder='little')
        print(f'{farbtiefe=}')

        kompression = int.from_bytes(f.read(4), byteorder='little')
        print(f'{kompression=}')

        image_size = kompression = int.from_bytes(f.read(4), byteorder='little')
        print(image_size)

        pixel_meter = int.from_bytes(f.read(8), byteorder='little')
        print(pixel_meter)

        farbpalette = int.from_bytes(f.read(4), byteorder='little')
        print(farbpalette)

        farbzeuch = int.from_bytes(f.read(4), byteorder='little')
        print(farbzeuch)



        f.read(offset - f.tell())
        data = f.read()


    else:
        exit('Keine BMP Datei')




    # for zeilen:
    #     for pixel_in_zeile:
    #         b =int.from_bytes(f.read(1))
    #         g =int.from_bytes(f.read(1))
    #         r =int.from_bytes(f.read(1))


fenster = tk.Tk()
pixel_breite = 1

zeilenbytes = breite_bitmap * 3
padding = (4 - (zeilenbytes % 4)) % 4
index = 0

reihenfolge = (
    range(hoehe_bitmap - 1, -1, -1) if bild_bottum_up else range(hoehe_bitmap)
)

for y in reihenfolge:
    for x in range(breite_bitmap):
        if index + 2 >= len(data):
            print(f'Abbruch: Index {index} überschreitet Datenlänge {len(data)}')
            break
        b = data[index]
        g = data[index + 1]
        r = data[index + 2]
        farbe = f"#{r:02x}{g:02x}{b:02x}"
        tk.Label(fenster, bg=farbe, width=pixel_breite, height=1).grid(row=y, column=x)
        index += 3
    index += padding

fenster.mainloop()