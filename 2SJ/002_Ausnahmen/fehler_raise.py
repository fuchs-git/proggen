# def bla(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError
#         print('Man darf nicht durch 0 teilen')
#         raise

def bla(a, b):
    if  b==0:
        raise ValueError(f"{b=} das darf nicht sein.", f'{a=}')
    return a/b

x = bla(5, 3)
y = bla(7, 0)

print(x + y)


# Fehler verketten
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Parameter b darf nicht 0 sein") from e

x = division(7, 3)
y = division(5, 0)

print(x + y)
