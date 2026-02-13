class Person:
    def __init__(self, name, alter, geschlecht):
        self.name = name
        self.alter = alter
        self._geschlecht = geschlecht

    @property
    def geschlecht(self):
        return self._geschlecht


    def __str__(self):
        if self._geschlecht == 'f':
            return f'{self.name}'
        return f'{self.name} {self.alter}'

    @property
    def alter(self):
        if self._geschlecht == 'f':
            raise ValueError("Das fragt man eine Dame nicht")
        return self._alter

    @alter.setter
    def alter(self, wert):
        self._alter = wert

a = Person('alice', 25, 'f')
b = Person('bob', 2, 'm')

print(a)
print(b)



b.geschlecht ='s'