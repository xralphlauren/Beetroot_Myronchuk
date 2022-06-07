import tkinter as tk


def entry():
    en.delete(0, tk.END)


root = tk.Tk()
root.geometry('800x600')

en = tk.Entry(root)    # полоса для ввода
en.grid(row=0, column=0)
en.insert(0, 'блаблабла')   # вставить текст в полосу

bt = tk.Button(root, text='del', command=entry)
bt.grid(row=1, column=1)
root.mainloop()
