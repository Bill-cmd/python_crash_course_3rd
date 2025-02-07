from random import randint

lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
lucky = []
my_ticket = [2, 4, 7, 'b']

print("Starting...")
times = 0
while lucky != my_ticket:
    for i in range(4):
        lottery_copy = lottery[:]
        char = lottery_copy[randint(0, len(lottery)-1)]
        #print(char)
        lottery_copy.remove(char) # remove the number from the list
        lucky.append(char)
    times += 1

print(f'You won after {times} tries!')
'''
for i in range(4):
    char = lottery[randint(0, len(lottery)-1)]
    #print(char)
    lottery.remove(char) # remove the number from the list
    lucky.append(char)

print(lucky)
'''