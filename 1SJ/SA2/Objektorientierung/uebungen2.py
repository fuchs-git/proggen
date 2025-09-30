import random
from random import randint


class Wuerfel:

    def __init__(self):
        self.augen = random.randint(1, 6)

    def __str__(self):
        return str(self.augen)

    def werfen(self):
        self.augen = random.randint(1, 6)
        return self.augen


class Wuerfelbecher:

    def __init__(self):
        self.w1 = Wuerfel()
        self.w2 = Wuerfel()
        self.w3 = Wuerfel()
        self.w4 = Wuerfel()
        self.w5 = Wuerfel()

    def werfen(self):
        self.__init__()

    def summe(self):
        # return int(str(self.w1)) + int(str(self.w2)) + int(str(self.w3)) + int(str(self.w4)) + int(str(self.w5))
        a = self.__str__()
        return sum([int(x) for x in a[1::2]])

    def __str__(self):
        return f"({self.w1},{self.w2},{self.w3},{self.w4},{self.w5})"

    def anzahl_6en(self):
        a = self.__str__()
        return [int(x) for x in a[1::2]].count(6)


wuerfel = Wuerfelbecher()
#
# print(wuerfel)
# print(wuerfel.summe())
# print(wuerfel.anzahl_6en())

fuenf_mal_sechs = Wuerfelbecher()
counter = 0
while fuenf_mal_sechs.anzahl_6en() != 5:
    fuenf_mal_sechs.werfen()
    counter += 1
# print(fuenf_mal_sechs, counter)

def mehrmals_versuchen(wb, versuche):
    for w in wb.w1,wb.w2,wb.w3,wb.w4,wb.w5:
        for i in range(versuche):
            if str(w) != "6":
                w.werfen()
        print(wb)





wb = Wuerfelbecher()
print(wb)
print(mehrmals_versuchen(wb, 4))


test = Wuerfelbecher()
for x in test.w1, test.w2:
    print(str(x))