from random import randint
from random import choice

print(randint(1, 10))
players = ['John', 'Jack', 'Jill', 'bill']
players_selected = []
i = 0
while i < 3:
    player = choice(players)
    print(player.title())
    players.remove(player)
    players_selected.append(player)
    i += 1

print(players_selected) 


