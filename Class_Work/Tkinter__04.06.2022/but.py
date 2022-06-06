import tkinter as tk


root = tk.Tk()
root.geometry('200x200')

bt1 = tk.Button(root, text='1')
bt2 = tk.Button(root, text='2')
bt3 = tk.Button(root, text='3')
bt4 = tk.Button(root, text='4')
bt5 = tk.Button(root, text='5')
bt6 = tk.Button(root, text='6')

bt1.grid(column=0, row=0, columnspan=4, sticky='EW')        # sticky - растянуть
bt2.grid(column=0, row=1)
bt3.grid(column=1, row=1, padx=10)                          # padx, pady - интервал между кнопками
bt4.grid(column=2, row=1)
bt5.grid(column=3, row=1)
bt6.grid(column=4, row=0, rowspan=2, sticky='NS')


root.mainloop()