import turtle as t
from time import sleep


def hallo(name1="Andreas", name2=""):
    if name1 == name2 or name2 == "":
        t.write("Hallo " + name1 + "!")
    else:
        t.write("Hallo " + name1 + " und " + name2 + "!")


# hallo("alice", "Bob")
hallo("Santa Claus")


def gestrichelt(leange):
    for i in range(leange // 10):
        t.pendown()
        t.forward(5)
        t.penup()
        t.forward(5)


def zeichne_seite_gepunktet(hoehe=100):
    gestrichelt(hoehe)
    t.left(90)


# hallo()

for i in range(4):
    zeichne_seite_gepunktet()
for i in range(4):
    zeichne_seite_gepunktet(110)
for i in range(4):
    zeichne_seite_gepunktet(111)

sleep(5)
