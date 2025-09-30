
def print_klein(*args,sep=' '):
    a = ''
    for elem in args:
        if type(elem) == type(""):
            a += str(elem).lower()
        else:
            a += str(elem)
        a += sep
    return a + "\b"



print(print_klein(1, 2, 3, 4, "Katze", 1 == 1, sep="#"))
