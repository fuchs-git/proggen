import turtle
import turtle as t
from time import sleep

t.speed(20)

def halbkreis(ecken, schritt, winkel):
    for i in range(ecken=60):
        t.forward(schritt)
        t.left(winkel / ecken)


halbkreis(60, 5, winkel=130)
halbkreis(60, 2, winkel=90)
t.right(75)
halbkreis(60, 2, winkel=90)
halbkreis(60, 5, winkel=130)

sleep(5)