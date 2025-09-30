import random
import os
import base64

def cls():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')
def flag():
    code = "ZnNid2l0e1czbGxfRDBuM19EdWNrX0h1bjczUn0="
    print(base64.b64decode(code).decode())

def game():
    x, y = 5, 5
    grid = [["" for x in range(x)] for y in range(y)]
    d1 = random.randint(0,x-1)
    d2 = random.randint(0,y-1)
    grid[d1][d2] = "X"

    for z in range(x):
        for i in range(y):
            print(f'{grid[z][i]}',end=" ")
        print("")

    zeile = int(input(f"In welcher Zeile ist die Ente?(0-{x-1}):"))
    spalte = int(input(f"In welcher Spalte ist die Ente?(0-{y-1}):"))

    if(zeile == d1 and spalte == d2):
        cls()
        print("Well Done!")

    else:
        print("Fail")
        exit()


for i in range(5):
    game()
flag()
