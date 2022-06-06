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
root.title('')
root.geometry('600x300+100+200')

s = ttk.Style()
s.configure('Big.TButton', font=('', 30), background='#000080')

lb = ttk.Label(root, text='6', font=('', 55))
lb.grid()

myFont = font.Font(size=30)
bt = tk.Button(root, text='бросить кубик', command=throw, font=myFont, background='green')
bt.grid()

bt2 = ttk.Button(root, text='бросить кубик ttk', command=throw, style='Big.TButton')
bt2.grid()

root.mainloop()
