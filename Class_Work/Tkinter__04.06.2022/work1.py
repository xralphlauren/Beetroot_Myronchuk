import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Window')
root.geometry('600x300+100+200')

s = ttk.Style()
s.configure('RED.TLabel', background='red')
s.configure('RED.TButton', background='red')

lb = ttk.Label(root, text='Я - лэйбл', style='RED.TLabel')
lb.grid()

btn = ttk.Button(root, text='Я кнопка', style='RED.TButton')
btn.grid()

btn2 = tk.Button(root, text='Я убийца платформы', command=root.destroy)
btn2.grid()

btn3 = tk.Button(root, text='Я убийца лейбла', command=lb.destroy)
btn3.grid()

root.mainloop()
