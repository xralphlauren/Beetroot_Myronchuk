import tkinter as tk


def password_entry():
    print(en_log.get())
    print(en_pass.get())
    en_log.delete(0, len(en_log.get()))
    en_pass.delete(0, len(en_pass.get()))


root = tk.Tk()
root.title('Entry password')

lb_log = tk.Label(root, text='Login', font='25')
lb_pass = tk.Label(root, text='Password', font='25')
lb_log.grid(row=0, column=0)
lb_pass.grid(row=1, column=0)

en_log = tk.Entry(root, font='25')
en_pass = tk.Entry(root, font='25')
en_log.grid(row=0, column=1)
en_pass.grid(row=1, column=1)

bt = tk.Button(root, text='Enter password', command=password_entry)
bt.grid(row=2,column=0, columnspan=2)

root.mainloop()
