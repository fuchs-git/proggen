import turtle as t
from time import sleep

def pyramide(hoehe, step):
    for i in range(hoehe):
        # Treppe Start
        t.left(90)
        t.forward(step)
        t.right(90)
        t.forward(step)

    for i in range(hoehe-1):
        t.right(90)
        t.forward(step)
        t.left(90)
        t.forward(step)

    # Treppe Ende
    t.right(90)
    t.forward(step)

    # Bodenlos
    t.right(90)
    t.forward((hoehe+hoehe-1)*step)
    t.hideturtle()


pyramide(5, 10)
# Ende
sleep(5)