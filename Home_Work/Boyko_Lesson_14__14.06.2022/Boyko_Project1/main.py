import math
import turtle as t


def zero():
    global current_position
    current_position += 70
    t.left(90)
    t.down()
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.left(180)
    t.up()
    t.setpos(current_position, 0)


def one():
    global current_position
    t.setpos(current_position, 50)
    current_position += 70
    t.left(45)
    t.down()
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.right(135)
    t.forward(100)
    t.left(90)
    t.up()
    t.setpos(current_position, 0)


def two():
    global current_position
    t.setpos(current_position, 100)
    current_position += 70
    t.down()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(135)
    t.forward(50)
    t.up()
    t.setpos(current_position, 0)


def three():
    global current_position
    t.setpos(current_position, 100)
    current_position += 70
    t.down()
    t.forward(50)
    t.right(135)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(135)
    t.forward(50)
    t.right(135)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(135)
    t.up()
    t.setpos(current_position, 0)


def four():
    global current_position
    t.setpos(current_position, 100)
    current_position += 70
    t.right(90)
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.up()
    t.left(90)
    t.forward(50)
    t.right(180)
    t.down()
    t.forward(100)
    t.up()
    t.left(90)
    t.setpos(current_position, 0)


def five():
    global current_position
    t.setpos(current_position + 50, 100)
    current_position += 70
    t.right(180)
    t.down()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.up()
    t.right(180)
    t.setpos(current_position, 0)


def six():
    global current_position
    t.setpos(current_position + 50, 100)
    current_position += 70
    t.right(135)
    t.down()
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.left(45)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.up()
    t.right(180)
    t.setpos(current_position, 0)

def seven():
    global current_position
    t.setpos(current_position, 100)
    current_position += 70
    t.down()
    t.forward(50)
    t.right(135)
    t.forward(70)
    t.left(45)
    t.forward(50)
    t.up()
    t.left(90)
    t.setpos(current_position, 0)


def eight():
    global current_position
    t.setpos(current_position, 50)
    current_position += 70
    t.left(90)
    t.down()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.up()
    t.setpos(current_position, 0)


def nine():
    global current_position
    t.setpos(current_position + 50, 50)
    current_position += 70
    t.left(180)
    t.down()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(45)
    t.forward(math.sqrt(50 * 50 + 50 * 50))
    t.up()
    t.left(135)
    t.setpos(current_position, 0)


lst_func = [zero, one, two, three, four, five, six, seven, eight, nine]
lst_code = list()
current_position = -300
t.up()
t.setpos(current_position, 0)
number = input('Input postal code: ')

for elem in number:
    lst_code.append(int(elem))

for i in range(len(lst_code)):
    lst_func[lst_code[i]]()
t.done()