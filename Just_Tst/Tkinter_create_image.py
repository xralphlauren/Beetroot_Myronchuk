import tkinter as tk
from PIL import ImageTk, Image



root = tk.Tk()
root.iconbitmap('C:\Python\Tkinter\ico\ph.ico')

my_img = ImageTk.PhotoImage(Image.open('C:\Python\Tkinter\png\ph.png'))
lb = tk.Label(image=my_img)
lb.grid(row=0, column=0)

root.mainloop()