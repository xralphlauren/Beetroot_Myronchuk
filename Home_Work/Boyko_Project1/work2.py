import turtle as t
import time

def space():
    global current_position
    t.up()
    current_position += 70
    t.setpos(current_position, 0)


def zero():
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    space()

def one():
    t.forward(50)
    t.left(90)
    t.down()
    t.forward(100)
    t.left(130)
    t.forward(70)
    t.left(140)
    space()


current_position = -300
t.up()
t.setpos(current_position, 0)

one()
zero()
one()
one()
zero()
time.sleep(30)