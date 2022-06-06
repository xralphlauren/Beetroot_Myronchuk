import tkinter as tk


def task_1():
    window_1 = tk.Tk()
    window_1.title('Window_1')
    window_1.geometry('960x500+0-0')    # Левая сторона вправо(-), влево(+)/Правая сторона верх(+), низ (-)

    window_2 = tk.Tk()
    window_2.title('Window_2')
    window_2.geometry('960x500+960+540')

    window_3 = tk.Tk()
    window_3.title('Window_3')
    window_3.geometry('960x500+960+0')

    window_4 = tk.Tk()
    window_4.title('Window_4')
    window_4.geometry('960x500+0+0')

    window_1.mainloop()


def task_2():
    window_1 = tk.Tk()
    window_1.title('Window_1')
    window_1.geometry('480x250+0-0')

    window_2 = tk.Tk()
    window_2.title('Window_2')
    window_2.geometry('480x250-0-0')

    window_3 = tk.Tk()
    window_3.title('Window_3')
    window_3.geometry('480x250-0+0')

    window_4 = tk.Tk()
    window_4.title('Window_4')
    window_4.geometry('480x250+0+0')

    window_5 = tk.Tk()
    window_5.title('Window_5')
    window_5.geometry('480x250+750+400')

    window_1.mainloop()


def task_3():
    window_1 = tk.Tk()
    window_1.title('Main window')

    width = window_1.winfo_screenwidth()
    height = window_1.winfo_screenheight()

    window_1.geometry(f'{width}x{height}')
    window_1.mainloop()


def task_4():
    window_1 = tk.Tk()
    window_1.title('Main window')

    width = window_1.winfo_screenwidth()
    height = window_1.winfo_screenheight()

    window_1.geometry(f'{int(width/2)}x{height}+0+0')
    window_1.mainloop()


def task_5():
    window_1 = tk.Tk()
    window_1.title('window_1')

    window_2 = tk.Tk()
    window_2.title('window_2')

    width = window_1.winfo_screenwidth()
    height = window_1.winfo_screenheight()

    window_1.geometry(f'{int(width/2)}x{height}+0+0')
    window_2.geometry(f'{int(width/2)}x{height}+{int(width/2)}+0')

    window_1.mainloop()


task_1()

