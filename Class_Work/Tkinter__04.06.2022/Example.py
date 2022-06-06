import tkinter
from tkinter.constants import *
from tkinter import ttk

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth='5', relief='raised')

tk = tkinter.Tk()

frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=5)      # рамка
frame.pack(fill=BOTH, expand=1)

label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)

button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)

tk.mainloop()