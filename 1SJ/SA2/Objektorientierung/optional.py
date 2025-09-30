text = """Justus,Haldenwang,53
Gabriele,Kochheim,38
Samantha,Eckhardt,49
Chantal,Mutz,56
Laura,Heymer,27
Lovis,Bradley,19
Rainer,Wolfrum,27"""


class Person:
    def __init__(self, vorname, name, alter):
        self.vorname = vorname
        self.name = name
        self.alter = alter
    def __str__(self):
        return f'{self.vorname}, {self.name}, {self.alter}'

def umwandeln(text):
    liste = text.split('\n')
    t = []
    for i in range(len(liste)):
        a,b,c =  liste[i].split(',')
        t.append(Person(a,b,int(c)))
    return t

p = umwandeln(text)
print(p)
print(*p, sep='\n')

print(sum(x.alter for x in p))
print(round(sum(x.alter for x in p) / len(p), 1))


name = ""
jung = 99
for person in p:
    if person.alter < jung:
        name = person.name
        jung = person.alter
print(name)

print(x.name for x in p if min(x.alter))


aaa = sorted([x.name for x in p])[0]
bbb = sorted([x.name for x in p])[-1]
print(aaa, bbb)
