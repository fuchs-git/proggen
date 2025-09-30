def f(x):
    if x == 3:
        print(15 / (3 - x))


try:
    f(3)
except ZeroDivisionError:
    print('Weltuntergang!!')
