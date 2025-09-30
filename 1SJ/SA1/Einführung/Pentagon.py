import turtle as t
from time import sleep

t.speed(0)

ecken = 3
for i in range(12):
    for j in range(3):
        for k in range(10):
            t.forward(50)
            t.left(360/ecken)
        t.forward(200)
    t.left(30)
sleep(5)