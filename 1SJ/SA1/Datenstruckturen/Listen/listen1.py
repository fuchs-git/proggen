
# letztes Element herausholen
liste = [1,2,3,4,5]

def int_to_string(int_liste:list):
    return [str(x) for x in int_liste]

print(int_to_string(liste))
print(" ".join(int_to_string(liste)))
