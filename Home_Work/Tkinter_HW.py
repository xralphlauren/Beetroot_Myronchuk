import tkinter as tk
from tkinter import ttk
import random


def scroll():
    lst_icons = ['♚', '♛', '♜', '♝', '♞', '♟']
    lst_slots = [random.choice(lst_icons) for i in range(3)]
    slot1['text'] = lst_slots[0]
    slot2['text'] = lst_slots[1]
    slot3['text'] = lst_slots[2]

    count_res = 0
    for i in lst_slots:
        if lst_slots.count(i) > count_res:
            count_res = lst_slots.count(i)
    if count_res == len(lst_slots):
        result_print['text'] = f'Поздравляем  вы выиграли ! ! !'
    elif count_res == 1:
        result_print['text'] = f'В молоко'
    else:
        result_print['text'] = f'Одинаковых слотов: {count_res}'


root = tk.Tk()
root.title('Slot machine')
root.geometry('800x600')

slot1 = tk.Label(root, text='Slot_1', font=('', 35))
slot2 = tk.Label(root, text='Slot_2', font=('', 35))
slot3 = tk.Label(root, text='Slot_3', font=('', 35))
slot1.grid(row=0, column=1)
slot2.grid(row=0, column=2)
slot3.grid(row=0, column=3)

result_print = tk.Label(root, text='Result: ', font=('', 25))
result_print.grid(row=2, column=4)


bt = tk.Button(root, command=scroll, font=('', 25), text='Scroll')
bt.grid(row=3, column=1, columnspan=3)

root.mainloop()
