import random

hand = ['камень', 'ножницы', 'бумага']
parties = []
count = 0

def get_hand(hand):
    return random.choice(hand)

def party(my, enemy):
    if my == enemy:
        return 0
    s = { 'камень' :{'бумага': -1, 'ножницы': 1},
          'ножницы':{'камень': -1, 'бумага': 1},
          'бумага' :{'ножницы': -1, 'камень': 1}}
    
    return s[my][enemy]

def score(my, enemy, parties):
    parties.append((my, enemy, party(my, enemy)))
    return sum(x[2] for x in parties)
    

for i in range(10):
    my = get_hand(hand)
    enemy = get_hand(hand)
    print(f'my:{my}, enemy:{enemy}, счет: {party(my, enemy)}')
    print(score(my, enemy, parties))
    print(parties)
