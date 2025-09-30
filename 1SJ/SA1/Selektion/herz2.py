import turtle as t
from time import sleep

t.speed(10)



def halbkreis(ecken, schritt, winkel):
    for i in range(ecken):
        t.forward(schritt)
        t.left(winkel / ecken)

# Startpunkt und Herzform
t.left(50)
halbkreis(60, 5, winkel=180)
t.right(100)
halbkreis(60, 5, winkel=180)

# Unten die Spitze des Herzens
t.forward(200)
t.left(92)
t.forward(220)
sleep(5)