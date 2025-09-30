'''
Schreiben Sie ein kleines Programm, das eine Binärdatei öffnet und deren Inhalt byteweise jeweils als zweistellige
Hexadezimalzahlen ausgibt. Dabei sollen jeweils 16 Byte in einer Zeile dargestellt werden. Die letzte ausgegebene Zeile
enthält dann die übrigen Bytes linksbündig.
'''

def hexview(data):
    print(f'Hex view:')
    for i in range(0, len(data),16):
        teil =data[i:i+16]
        #hex_zeile = ' '.join(('{:02x}'.format(byte) for byte in teil))
        hex_zeile = ' '.join((f'{byte:02x}' for byte in teil))
        print(f'{hex_zeile}')



with open('datein.bin', 'rb') as f:
    data = f.read()

hexview(data)
