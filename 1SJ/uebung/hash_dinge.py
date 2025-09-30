class Stiefel:
    def __init__(self, groesse):
        self.groesse = groesse

    def __eq__(self, other:'Stiefel'):
        return self.groesse == other.groesse

    def __hash__(self):
        return hash(self.groesse)


paar1 = Stiefel(43)
paar2 = Stiefel(43)

print('Gleichheit:', paar1 == paar2)
print('Ident:', paar1 is paar2)
print(f'{id(paar1)=}\n{id(paar2)=}')
print(f'{hash(paar1)=}\n{hash(paar2)=}')


