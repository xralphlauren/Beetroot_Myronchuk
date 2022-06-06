import tkinter as tk


root = tk.Tk()
root.title('Я платформа')  # название платформы ( окошка )
root.geometry('300x300+100+200')  # размер изначального окно (300х300 - размер окна; +100, +200 - расположение на екр)

rt1 = tk.Tk()
rt1.geometry('900x10+400-200')

p = []
for i in range(10):
    p.append(tk.Tk())

s = 10
for pl in p:
    s = s + 100
    pl.geometry(f'{s}x300+{s}+200')

root.mainloop()  # зацыкливает включение платформы ( если используется две платформы, нужен один луп )
