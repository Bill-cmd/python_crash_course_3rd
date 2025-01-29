motorcyles = ['honda', 'yamaha', 'suzuki']
print(motorcyles)

motorcyles[0] = 'ducati'
print(motorcyles)

motorcyles.append('ducati')
print(motorcyles)

motorcyles.insert(2, 'Natasha')
print(motorcyles)

del motorcyles[0]
print(motorcyles)

popped_motorcyles = motorcyles.pop()
print(motorcyles)
print(popped_motorcyles)

last_owned = motorcyles.pop()
print(f"The last motorcyle I owned was a {last_owned.title()}.")
print(motorcyles)

