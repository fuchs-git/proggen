def nachfolger(x):
    return x+1

dinge = [1,2,3,4,5]

neue_liste = []
for e in dinge:
    neue_liste.append(nachfolger(e))

neue_liste2 = list(map(nachfolger,dinge))

print(dinge)
print(neue_liste)
print(neue_liste2)