import tkinter as tk


root = tk.Tk()
bt = tk.Button(root, text='кнопка')
bt.grid()

print(bt['text'])
print(bt['foreground'])
bt['foreground'] = '#FF0EE0'
print(bt['foreground'])

root.mainloop()