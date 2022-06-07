import tkinter as tk



class Table:

    def __init__(self, root, table):

        total_rows = len(table)
        total_columns = len(table[0])

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = tk.Entry(root, width=20, fg='blue',
                                  font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, table[i][j])


# take the data
lst = [(1, 'Raj', 'Mumbai', 19),
       (2, 'Aaryan', 'Pune', 18),
       (3, 'Vaishnavi', 'Mumbai', 20),
       (4, 'Rachna', 'Mumbai', 21),
       (5, 'Shubham', 'Delhi', 21)]


# create root window
root = tk.Tk()
t = Table(root, lst)
root.mainloop()
