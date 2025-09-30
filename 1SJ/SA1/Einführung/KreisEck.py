import turtle as t

a=100
b=50
ecken = 72
t.speed(0)

for i in range(ecken):
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.right(360 / ecken)

sleep(1)