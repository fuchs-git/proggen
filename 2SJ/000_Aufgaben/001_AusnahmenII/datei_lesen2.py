import sys
# Ausführung im Terminal

def datei_lesen(datei):
    try:
        with open(datei, 'r', encoding='utf-8') as f:
            print('Inhalt der Datei:')
            print(f.read())
    except FileNotFoundError as e:
        print(f'Welche Datei wurde nicht gefunden? {e.filename}')
        print(f'Welchen Fehlercode hat das Betriebssystem zurückgegeben? {e.errno}')
        print(f'Welche Beschreibung gibt es zu diesem Fehlercode? {e.strerror}')
        print(f'Die Datei {e.filename} wurde nicht gefunden. Fehlernummer {e.errno} ({e.strerror}).')

datei_lesen(sys.argv[1])