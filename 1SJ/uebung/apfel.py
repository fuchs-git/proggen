class Apfel:
    def __init__(self, sorte:str):
        self.sorte = sorte

    def __eq__(self, other:'Apfel'):
        return self.sorte == other.sorte and type(other) == type(self)

class Birne:
    def __init__(self, sorte:str):
        self.sorte = sorte

    def __eq__(self, other:'Birne'):
        return self.sorte == other.sorte and type(other) == type(self)

a1 = Apfel('Süße Versuchung')
a2 = Apfel('Süße Versuchung')

b1 = Birne('Süße Versuchung')
b2 = Birne('Süße Versuchung')

print(a1 == a2)
print(b1 == b2)
print(a1 == b1)