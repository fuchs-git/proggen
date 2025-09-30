with open("input", "r") as f:
    file = f.read()


def aufsteigend(lst:list)->list:
    for i in range(len(lst) - 1):
        if int(lst[i]) > int(lst[i + 1]):
            return False
    return True


def absteigend(lst:list):
    for i in range(len(lst) - 1):
        if int(lst[i]) < int(lst[i + 1]):
            return False
    return True

gut = []
zeile = file.split("\n")
for elem in zeile:
    liste = elem.split()
    if aufsteigend(liste) or absteigend(liste):
        check = True
        for i in range(len(liste)-1):
            if abs(int(liste[i]) - (int(liste[i+1]))) >3 or abs(int(liste[i]) - (int(liste[i+1]))) == 0:
                check = False
                break
        if check:
            gut.append(liste)

print(len(gut))