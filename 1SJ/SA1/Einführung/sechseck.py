import turtle
from time import sleep

ecken = 360
for i in range(ecken):
    turtle.forward(1)
    turtle.left(360/ecken)

sleep(1)