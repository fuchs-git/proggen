# Schreiben Sie ein Programm, das den Benutzer nach dem Namen einer Datei fragt und versucht, diese Datei zu öffnen
# und ihren Inhalt auf den Bildschirm auszugeben. Beachten Sie dabei folgende Anforderungen:

def datei_lesen():
    i = input('Bitte geben Sie den Dateinamen ein:')
    try:
        with open(i, 'r', encoding='utf-8') as f:
            print('Inhalt der Datei:')
            print(f.read())
    except FileNotFoundError as e:
        print(f'Welche Datei wurde nicht gefunden? {e.filename}')
        print(f'Welchen Fehlercode hat das Betriebssystem zurückgegeben? {e.errno}')
        print(f'Welche Beschreibung gibt es zu diesem Fehlercode? {e.strerror}')
        print(f'Die Datei {e.filename} wurde nicht gefunden. Fehlernummer {e.errno} ({e.strerror}).')

datei_lesen()