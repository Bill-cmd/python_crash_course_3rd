from random import randint

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

i = 0
while i < 4:
    char = lottery[randint(0, 14)]
    print(char)
    lottery.remove(char) # remove the number from the list
    i += 1

