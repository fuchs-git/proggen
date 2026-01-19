import re

class Auswerter:
    def __init__(self, dateiname):
        self.dateiname = dateiname
        self.datenstruktur = []
        print('hallo')
        self.einlesen()


    def einlesen(self):
        print('hallo')
        with open(self.dateiname) as f:
            datei = f.read()

        pattern = r'^(.{19}) -- (.*?)$'
        treffer = re.findall(pattern, datei, flags=re.MULTILINE)
        print(treffer)

test = Auswerter('data.txt')
