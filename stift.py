class Stift:
    def __init__(self, material):
        self.farbe = None
        self.material = material

    def malen(self):
        if self.farbe:
            print(rf'''ich male {self.farbe}''')
        else:
            print('ich male')


class RoterStift(Stift):
    def __init__(self, *args, **kwargs):
        Stift.__init__(self, *args, **kwargs)
        self.farbe = 'rot'

s = Stift('Bambus')
s.malen()

r = RoterStift(material='Holz')
r.malen()
print(r.material)
