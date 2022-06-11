import tkinter as tk


def press(event):
    print(event)

root = tk.Tk()
root.geometry('300x300')

bt1 = tk.Button(root, text='Кнопка')
bt1.pack()

lb1 = tk.Label(root, text='Надпись')
lb1.pack()
lb1.bind('<f>', press)
lb1.bind("<ButtonPress-1>", press)

root.mainloop()