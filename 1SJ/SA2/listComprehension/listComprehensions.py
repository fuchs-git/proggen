# import random
# import string
#
# liste = [x for x in range(10)]
# print(liste)
#
# liste = [x for x in "Hallo Welt!"]
# print(liste)
#
# liste = [x for x in [1,2,3,4]]
# print(liste)
#
# liste = [x % 2 == 0 for x in range(20)]
# liste = ["Hallo Welt" if x == 8 else x  for x in range(20) if x % 2 == 0]
#
# print(liste)
#
# print("Liste der ersten 100 Quadratzahlen")
# liste = [x*x for x in range(100) if "1" in str(x*x)]
# print(liste)
#
# liste = [x + y for x in range(10,60,10) for y in range(1,6) if x>y*10]
# print(liste)
#
# liste = [x for x in range(100,1000) if "5" in str(x) and "7" in str(x)]
# print(liste)
#
# liste = [random.randint(1, 6) for _ in range(10)]
# print(liste)
#
# liste = []
# anzahl = 0
# while liste.count(6) < 3:
#     liste = [random.randint(1, 6) for _ in range(10)]
#     anzahl += 1
# print(liste, anzahl)
#
# print(string.ascii_uppercase)
#

print([ x for x in range(1,11)])
print([ 2**x for x in range(0,11) ])
namen = ['Alice', 'Bob', 'Charlie', 'Doris', 'Clare', 'Ernie', 'Bert', 'Chris']
liste = [ x[0] for x in namen]
print([len(x) for x in namen])
print([x[0] + "*" * (len(x)-1) for x in namen])
