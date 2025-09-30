'''
Erstellen Sie ein bytes-Literal, das möglichst viel Obst und Gemüse enthält!

Also ungefähr so. Aber natürlich ist uns das noch deutlich zu wenig 😋

print(b'\xf0\x9f\x8d\x8f, '
      b'\xf0\x9f\x8d\x8c, '
      b'\xf0\x9f\x8d\x93...'.decode('utf-8'))
'''

print(b'\xf0\x9f\x8d\x8f, ' 
      b'\xf0\x9f\x8d\x8c, ' 
      b'\xf0\x9f\x8d\x93...'.decode('utf-8'))

print(  b'\xf0\x9f\x8d\x90'
        b'\xf0\x9f\x8d\x95'
        b'\xf0\x9f\x8d\x94'
        b'\xf0\x9f\x8d\x9f'
        b'\xf0\x9f\x8c\xad'
        b'\xf0\x9f\x8d\xbf'
        b'\xf0\x9f\xa5\x93'.decode('utf8'))

'''
Wahrscheinlich waren Sie bei der letzten Aufgabe fleißig und haben viel Obst und Gemüse gesammelt.
Versuchen jetzt, die Bytes dynamisch, also mit einer Schleife zu erzeugen.
Wenn Sie den 🍄 hinzunehmen, liegen mit ihm 16 Emojis aus dem Bereich Obst und Gemüse direkt hintereinander im Unicode 😉
'''

obst = []
for item in '🍇🍉🍋‍🟩🍍🥭🍓🍒🍑🍎🫐🍅🫒🍆🌽🌶️':
    obst.append(item.encode('utf8'))
print(*obst)

obst2 = [i.encode('utf8') for i in '🍇🍉🍋‍🟩🍍🥭🍓🍒🍑🍎🫐🍅🫒🍆🌽🌶️🍄']
print(f'{obst2=}')
print('Obst2=',*[i.decode('utf8') for i in obst2])


start = '🍄'.encode('utf8')

for i in range(16):
    ba = bytearray(start)
    if ba[-1]+1 == 256:
        ba[-2] = ba[-2]+1
    ba[-1] = (ba[-1]+i) %256
    print(ba, ba[-1], ba.decode('utf8'))
