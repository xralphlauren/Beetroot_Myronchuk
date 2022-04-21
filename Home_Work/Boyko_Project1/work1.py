import turtle as t
import time

def zero():
    t.up()
    t.forward(20)
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(100)
    t.up()
    t.left(90)
    t.forward(50)

def one():
    t.up()
    t.forward(70)
    t.left(90)
    t.down()
    t.forward(100)
    t.left(130)
    t.forward(70)
    t.up()
    t.left(180)
    t.forward(70)
    t.right(130)
    t.forward(100)
    t.left(90)


current_position = -300
t.up()
t.setpos(current_position, 0)

one()
zero()
one()
one()
zero()
time.sleep(30)