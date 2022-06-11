import tkinter as tk
import pult


def shw_ch():
    display['text'] = pult.controller.current_channel()


def check_ch(n):
    if n <= len(pult.CHANNELS):
        pult.controller.turn_channel(n)
        shw_ch()
    else:
        display['text'] = f'Канала под номером {n} в данный момент не существует'


def add_channel():
    inp = input('Введите название каналов которые хотите добавить: ').replace(' ', '').split(',')
    for ch in inp:
        pult.CHANNELS.append(ch)



root = tk.Tk()
root.title('TV pult')

fr1 = tk.Frame(root, border=15, relief='ridge')
fr2 = tk.Frame(root)
fr3 = tk.Frame(root)
fr4 = tk.Frame(root)
fr5 = tk.Frame(root)
fr_lst = [fr1, fr2, fr3, fr4, fr5]
for i in fr_lst:
    i.pack()

display = tk.Label(fr1, height=10, width=45, text=pult.controller.current_channel(), font=50)
display.pack()

bt1 = tk.Button(fr2, height=5, width=15, text='1', font=50, command=lambda: check_ch(1))
bt2 = tk.Button(fr2, height=5, width=15, text='2', font=50, command=lambda: check_ch(2))
bt3 = tk.Button(fr2, height=5, width=15, text='3', font=50, command=lambda: check_ch(3))
bt4 = tk.Button(fr2, height=5, width=15, text='4', font=50, command=lambda: check_ch(4))
bt5 = tk.Button(fr2, height=5, width=15, text='5', font=50, command=lambda: check_ch(5))
bt6 = tk.Button(fr2, height=5, width=15, text='6', font=50, command=lambda: check_ch(6))
bt7 = tk.Button(fr2, height=5, width=15, text='7', font=50, command=lambda: check_ch(7))
bt8 = tk.Button(fr2, height=5, width=15, text='8', font=50, command=lambda: check_ch(8))
bt9 = tk.Button(fr2, height=5, width=15, text='9', font=50, command=lambda: check_ch(9))
btdigit = [bt1, bt2, bt3, bt4, bt5, bt6, bt7, bt8, bt9]
r = 0
c = 0
for i in btdigit:
    i.grid(row=r, column=c)
    if c == 2:
        c = 0
        r += 1
        continue
    c += 1

btadd = tk.Button(fr3, height=5, width=15, text='add channel', font=15, command=lambda:
                  [add_channel(), shw_ch()])
bt_previous = tk.Button(fr3, height=5, width=15, text='Previous channel', font=15, command=
                        lambda: [pult.controller.previous_channel(), shw_ch()])
bt_next = tk.Button(fr3, height=5, width=15, text='Next channel', font=15, command=
                    lambda: [pult.controller.next_channel(), shw_ch()])

bt_previous.grid(row=0, column=0)
btadd.grid(row=0, column=1)
bt_next.grid(row=0, column=2)


bt_first = tk.Button(fr4, height=5, width=23, text='First channel', font=50, command=lambda:
                     [pult.controller.first_channel(), shw_ch()])
bt_Last = tk.Button(fr4, height=5, width=23, text='Last channel', font=50, command=lambda:
                     [pult.controller.last_channel(), shw_ch()])
bt_first.grid(row=0, column=0)
bt_Last.grid(row=0, column=1)


root.mainloop()
