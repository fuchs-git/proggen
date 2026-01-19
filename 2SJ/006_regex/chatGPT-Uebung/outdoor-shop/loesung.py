import re

class Produkt:
    def __init__(self, id, name, beschreibung, ausmass, preis):
        self.id = id
        self.name = name
        self.beschreibung = beschreibung
        self.ausmass = ausmass
        self.preis = preis

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.preis}'

    def __gt__(self, other: 'Produkt'):
        return self.preis > other.preis


with open('SHOP.html', encoding='UTF8') as f:
    datei = f.read().strip().replace('\n', ' ')
print(len(datei))


# Aufgabe 2

pattern2 = r'<div data-ref-id="\w?\d{8}">'
treffer = re.findall(pattern2, datei)
#print(len(treffer))

# Aufgabe 3
pattern3 = r'<div data-ref-id="(\w?\d{8})">.*?<span class="notranslate plp-price-module__product-name">([A-ZÄÖÅ/ ].*?)</span>'
treffer = re.findall(pattern3, datei)

#for id, name in treffer:
#    print(id, name)


# Aufgabe 4
pattern4 = (r'<div data-ref-id="(\w?\d{8})">.*?'
            r'<span class="notranslate plp-price-module__product-name">([A-ZÄÖÅ/ ].*?)</span>.*?'
            r'<span class="plp-price-module__description">(.*?), (\d.*?) ?cm</span>')

treffer = re.findall(pattern4, datei)

#for id, name, beschreibung, y in treffer:
#    print(id, name, beschreibung, y)

# Aufgabe 5
pattern5 = pattern4 + r'.*?<span class="plp-price__sr-text">Preis ([\d]{1,4}\.[\d]{0,2})€</span>'

treffer = re.findall(pattern5, datei)


produkt_liste = []
for id, name, beschreibung, y, preis in treffer:
    #print(id, name, beschreibung, y, float(preis))
    produkt_liste.append(Produkt(id,name,beschreibung,y,round(float(preis),2)))

#for produkt in sorted(produkt_liste, reverse=True):
#    print(produkt)

print('------------------------------------')
# <span class="plp-price-module__description">Tarp, reißfest, 25x33 cm</span>
pattern = r'<span class="(plp-price-module__description)">([^<]+)</span>'
treffer = re.finditer(pattern, datei)

for t in treffer:
    anfang, ende = t.span(2)
    print(t.group(2), ende-anfang)


