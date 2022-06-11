import tkinter as tk
root = tk.Tk()


clip = root.clipboard_get()
print(clip)


f = open('buffer.txt', 'a')
f.write(clip)
f.close()