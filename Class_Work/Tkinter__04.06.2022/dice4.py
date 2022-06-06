import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import random

di = ('', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅')


def throw():
    vedro = []
    summ = 0
    for i in range(int(kolvo.get())):
        dice = random.randint(1, 6)
        summ += dice
        vedro.append(di[dice])
    lb_sum['text'] = str(summ)
    lb['text'] = ' '.join(vedro)
    # print(kolvo.get())
    # kolvo.set(str(summ))


root = tk.Tk()
root.title('Я платформа')
root.geometry('600x300+100+200')
# задание интерфейса
s = ttk.Style()
s.configure('Big.TButton', font=('', 25))
s.configure('Big.TCombobox', font=('', 25))
lb = ttk.Label(root, text='', font=('', 40))
lb.grid(column=0, row=1, sticky='WE')
lb_sum = ttk.Label(root, text='SUM', font=("", 30))
lb_sum.grid(column=1, row=0, padx=10, pady=3)
lb_sum['text'] = '0'
bt = ttk.Button(root, text='бросить кубик', style='Big.TButton', command=throw)
bt.grid(column=0, row=0, sticky='WE')
kolvo = tk.StringVar()
# en_kolvo = ttk.Entry(root, textvariable=kolvo)
# en_kolvo.grid(row = 0, column = 2, sticky = 'W')
cmb_kolvo = ttk.Combobox(root,
                         textvariable=kolvo,
                         width=4,
                         font="Verdana 16 bold",
                         style='Big.TCombobox')

cmb_kolvo['values'] = [str(x) for x in range(20)]
cmb_kolvo.grid(row=0, column=3, sticky='E')
kolvo.set('3')
root.mainloop()