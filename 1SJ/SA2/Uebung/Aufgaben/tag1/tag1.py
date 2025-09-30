with open("day_1_input.txt", "r") as f:
    tag = f.read()
x = tag.split()

a = 0
summe = 0
liste1 = x[::2]
liste2 = x[1::2]

liste1.sort()
liste2.sort()

for i in range(len(liste1)):
    a = abs(int(liste1[i]) - int(liste2[i]))
    print(f'{liste1[i]:6} {liste2[i]:6} = {a}')
    summe += a

print(summe)



