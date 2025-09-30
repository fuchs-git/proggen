class Land:
    def __init__(self, name:str, einwohner:int, flaeche:int):
        self.name = name
        self.einwohner = einwohner
        self.flaeche = flaeche

    def ew_einheiten(self):
        if self.einwohner >= 1_000_000: return f'~ {self.einwohner / 1_000_000:.0f} Mio. Ew'
        elif self.einwohner >= 1_000: return f'~ {self.einwohner / 1_000:.0f} Tsd. Ew'
        else: return f'~ {self.einwohner} Ew'

    def __str__(self):
        return  f'{self.name} ({self.ew_einheiten()}, {self.flaeche:_}km²)'

    def __repr__(self):
        return  f'{self.name}'

takatukaland = Land("Takatukaland", 123, 1_000)  # Land unter 1000 Ew
gondor = Land("Gondor", 56_789, 1_000_000)  # Land zwischen 1_000 und 1_000_000
sokovia = Land("Sokovia", 12_345_678, 9876)  # Land ab 1_000_000

fiktiv = {takatukaland, gondor, sokovia}
print(fiktiv)  # Darstellung in einer Datenstruktur

for land in fiktiv:
    print(land)  # Einzeldarstellung

with open('countries.txt', 'r') as f:
    f.readline()
    countries = f.read()

real = []
for line in countries.split('\n'):
# Country Population YearlyChange	NetChange	Density(P/Km²)	LandArea(Km²)	Migrants (net)	Fert. Rate	Med. Age	Urban Pop %	World Share
    country, population, yearlyChange, netChange, density,landArea,*rest =line.split('\t')
    real.append(Land(country, int(population.replace(',','')),int(landArea.replace(',',''))))

# print(real)
# for land in real:
#    print(land)  # Einzeldarstellung