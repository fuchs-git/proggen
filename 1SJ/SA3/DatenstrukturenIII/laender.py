# Erzeugen Sie eine Funktion land_ausgeben, welche einen Ländernamen übergeben bekommt. Die Funktion prüft, ob das Land
# in laender enthalten ist. Wenn ja, wird das Land hübsch formatiert ausgegeben (Beispiel siehe unten), wenn nein, macht
# die Funktion nichts. Die Ausgabe Einwohnerzahl soll bei Ländern ab einer Million Einwohnern auf ganze Millionen und
# bei Ländern ab eintausend aber unter einer Million Einwohner auf ganze Tausend gerundet werden.


def land_ausgeben(land):
    if land in laender:
        print(f'{land} ({ew_filter(land)}, {laender[land]['Fläche']:_} km²)')


def ew_filter(land):
    if laender[land]['Einwohner'] >= 1_000_000:
        return f'~ {laender[land]['Einwohner'] / 1_000_000:.0f} Mio. Ew'
    elif laender[land]['Einwohner'] >= 1_000:
        return f'~ {laender[land]['Einwohner'] / 1_000:.0f} Tsd. Ew'
    else:
        return f'~ {laender[land]['Einwohner']} Ew'


# Erzeugen Sie ein zunächst leeres Dictionary laender.
laender = {}

# Fügen Sie zu laender die Länder mit folgenden Daten hinzu:

laender['Takatukaland'] = {'Einwohner': 123, 'Fläche': 1_000}
laender['Gondor'] = {'Einwohner': 56_789, 'Fläche': 1_000_000}
laender['Sokovia'] = {'Einwohner': 12_345_678, 'Fläche': 9876}

# land_ausgeben("Takatukaland")
# land_ausgeben("Gondor")
# land_ausgeben("Sokovia")
# land_ausgeben("Kleinaitingen")

with open('countries.txt', 'r') as f:
    f.readline()
    countries = f.read()

# Lassen Sie das Dictionary laender und die Anzahl der Länder darin ausgeben (es sollten 237 sein).
for line in countries.split('\n'):
    # Country Population YearlyChange	NetChange	Density(P/Km²)	LandArea(Km²)	Migrants (net)	Fert. Rate	Med. Age	Urban Pop %	World Share
    country, population, x, y, z, landArea, *rest = line.split('\t')
    laender[country] = {'Einwohner': int(population.replace(',', '')),
                        'Fläche': int(landArea.replace(',', ''))}
# print(len(laender))

# Bestimmen Sie mit der Funktion max das Land aus laender, welches die meisten Einwohner hat! Damit das nicht Simbabwe
# wird, müssen Sie der Funktion max mitteilen, dass Sie den Größenvergleich nach Einwohnerzahl benötigen und nicht nach
# Name (Sie müssen sich klarmachen, dass max über das Dictionary iteriert, um das größte Element zu finden. Wenn man über
# Dictionaries iteriert, erhält man erst mal nur die Keys …). Es gibt mehrere Varianten, dies umzusetzen.

land_ausgeben(max(laender, key=lambda x: laender.get(x).get('Einwohner')))
land_ausgeben(max(laender, key=lambda x: laender.get(x).get('Fläche')))


# Erzeugen Sie mit einer Dictionary-Comprehension ein neues Dictionary aller Länder, die mindestens so groß wie
# Frankreich (France) und kleiner als Deutschland (Germany) sind (jeweils nach Einwohnern, das sollten 4 Länder sein)

auswahl = {
    land: daten
    for land, daten in laender.items()
    if daten['Einwohner'] >= laender['France']['Einwohner'] and daten['Einwohner'] < laender['Germany']['Einwohner']
}
sortiert = sorted(auswahl, key=lambda x: auswahl[x]['Einwohner'], reverse=True)
print(f'{" Aufgabe 6 ":-^50}', )
for i, land in enumerate(sortiert):
    print(i + 1, end='\t')
    land_ausgeben(land)

# Erzeugen Sie mit einer Dictionary-Comprehension ein neues Dictionary aller Länder, die mindestens so groß wie
# Deutschland (Germany) und kleiner als Frankreich (France) sind (jeweils nach Fläche, das sollten 16 Länder sein).

auswahl = {
    land: daten
    for land, daten in laender.items()
    if daten['Fläche'] >= laender['Germany']['Fläche'] and daten['Fläche'] < laender['France']['Fläche']
}

sortiert = sorted(auswahl, key=lambda x: auswahl[x]['Fläche'], reverse=True)
print(f'{" Aufgabe 7 ":-^50}', )
for i, land in enumerate(sortiert):
    print(i + 1, end='\t')
    land_ausgeben(land)

# Erzeugen Sie mit einer Dictionary-Comprehension ein neues Dictionary aller Länder, die kleiner als Deutschland (Germany)
# nach Fläche, aber größer als Frankreich (France) nach Einwohnerzahl sind (das sollten 4 Länder sein).
sortiert = {
    land: daten
    for land, daten in laender.items()
    if daten['Einwohner'] > laender['France']['Einwohner'] and daten['Fläche'] < laender['Germany']['Fläche']
}
print(f'{" Aufgabe 8 ":-^50}', )
for i, land in enumerate(sortiert):
    print(i + 1, end='\t')
    land_ausgeben(land)
