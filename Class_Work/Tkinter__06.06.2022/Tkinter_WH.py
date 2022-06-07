import tkinter as tk
import wh


class Table:
    def __init__(self, root, table):
        self.attrlist = ["name", "status", "salary", "pay_basis", "position_title"]
        self.N = 0
        self.step = 10
        self.table = table
        self.root = root

        for n, s in enumerate(self.table[self.N:self.N + self.step]):
            for j, f in enumerate(self.attrlist):
                self.e = tk.Entry(root, width=20, fg='blue',
                                  font=('Arial', 16, 'bold'))
                self.e.grid(row=n, column=j)
        self.plus10()

    def clean(self):
        # очищает формы
        for wi in self.root.winfo_children():
            wi.delete(0, tk.END)

    def minus10(self):

        if self.N + self.step - 10 < 1:
            return

        self.N -= 10
        self.clean()
        # записывает в формы 10 человек
        all_wi = self.root.winfo_children()
        for s in self.table[self.N:self.N + self.step]:
            for f in self.attrlist:
                w = all_wi.pop(0)
                w.insert(0, getattr(s, f))

    def plus10(self):
        if self.N + self.step + 10 < len(self.table):
            self.N += 10
        self.clean()

        # записывает в формы 10 человек
        all_wi = self.root.winfo_children()
        for s in self.table[self.N:self.N + self.step]:
            for f in self.attrlist:
                w = all_wi.pop(0)
                w.insert(0, getattr(s, f))


w = wh.WH('wh2017.csv')

# create root window
root = tk.Tk()

fr = tk.Frame(root)
fr.grid(row=0, column=0, columnspan=2)

t = Table(fr, w.sotr)  # [ Person0, Person1, ... ] # Person0.salary

bt1 = tk.Button(root, text='-10', command=t.minus10)
bt1.grid(row=1, column=0)

bt2 = tk.Button(root, text='+10', command=t.plus10)
bt2.grid(row=1, column=1)

root.mainloop()

