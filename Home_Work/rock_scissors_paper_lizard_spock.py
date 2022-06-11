import tkinter as tk
import random


class game:
    my_point = 0
    pc_point = 0

    def __init__(self):
        self.dct = {
                    'rock': ['scissors', 'lizard'],
                    'paper': ['rock', 'spock'],
                    'scissors': ['paper', 'lizard'],
                    'lizard': ['spock', 'paper'],
                    'spock': ['rock', 'scissors']
                    }

    def machine_rand(self):
        self.machine_choice = random.choice(list(self.dct))
        lb_2['text'] = f'Machine choice: {self.machine_choice}'

    def result(self):
        if self.machine_choice in self.dct[self.player_choice]:
            lb_3['text'] = 'You win'
            self.__class__.my_point += 1
            lb_4['text'] = f'You point: {self.__class__.my_point}'
        elif self.player_choice in self.dct[self.machine_choice]:
            lb_3['text'] = 'You loose'
            self.__class__.pc_point += 1
            lb_5['text'] = f'PC point: {self.__class__.pc_point}'
        else:
            lb_3['text'] = 'Draw'

    def rock(self):
        self.player_choice = 'rock'
        lb_1['text'] = f'Your choice: rock'
        self.machine_rand()
        self.result()

    def paper(self):
        self.player_choice = 'paper'
        lb_1['text'] = f'Your choice: paper'
        self.machine_rand()
        self.result()

    def scissors(self):
        self.player_choice = 'scissors'
        lb_1['text'] = f'Your choice: scissors'
        self.machine_rand()
        self.result()

    def lizard(self):
        self.player_choice = 'lizard'
        lb_1['text'] = f'Your choice: lizard'
        self.machine_rand()
        self.result()

    def spock(self):
        self.player_choice = 'spock'
        lb_1['text'] = f'Your choice: spock'
        self.machine_rand()
        self.result()


g = game()

root = tk.Tk()
root.title("game")


fr = tk.Frame(root, border=2, relief='ridge')
fr.grid(column=0, columnspan=5, row=0, sticky='WE')


lb_1 = tk.Label(fr, text='Your choice: ', font='30')
lb_2 = tk.Label(fr, text='Machine choice: ', font='30')
lb_3 = tk.Label(fr, text='Result: ', font='30')
lb_4 = tk.Label(fr, text='Your point: 0', font='40')
lb_5 = tk.Label(fr, text='PC point: 0', font='40')
lb_1.grid(row=0, column=0, sticky='W')
lb_2.grid(row=1, column=0, sticky='W')
lb_3.grid(row=2, column=0, sticky='W')
lb_4.grid(row=3, column=0, sticky='W')
lb_5.grid(row=3, column=2, sticky='W')


bt_rock = tk.Button(root, text='rock', font='25', command=g.rock)
bt_paper = tk.Button(root, text='paper', font='25', command=g.paper)
bt_scissors = tk.Button(root, text='scissors', font='25', command=g.scissors)
bt_lizard = tk.Button(root, text='lizard', font='25', command=g.lizard)
bt_spock = tk.Button(root, text='spock', font='25', command=g.spock)
bt_rock.grid(row=4, column=0)
bt_paper.grid(row=4, column=1)
bt_scissors.grid(row=4, column=2)
bt_lizard.grid(row=4, column=3)
bt_spock.grid(row=4, column=4)

root.mainloop()
