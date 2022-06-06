import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import random

di = ('⚀', '⚁', '⚂', '⚃', '⚄', '⚅')


def throw():
    vedro = []
    for i in range(5):
        dice = random.choice(di)
        vedro.append(dice)

    lb['text'] = ' '.join(vedro)


root = tk.Tk()
root.title('Я платформа')
root.geometry('600x300+100+200')

s = ttk.Style()
s.configure('Big.TButton', font=('', 25))

fr = ttk.Frame(root)
fr.grid()

lb = ttk.Label(fr, text='6', font=('', 40))
lb.grid(column=0, row=1, sticky='WE')

lb_sum = ttk.Label(root, text='SUM', font=('', 30))
lb_sum.grid(column=1, row=0, padx=10)

bt = ttk.Button(fr, text='бросить кубик', style='Big.TButton', command=throw)
bt.grid(column=0, row=0, sticky='WE')

root.mainloop()