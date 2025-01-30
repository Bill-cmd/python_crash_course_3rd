sandwich_orders = ['Bacon', 'pastrami', 'Bagel toast', 'pastrami', 'Crisp', 'pastrami']
finished_sandwich = []

print("The deli's pastrami is sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(f"\nThe list of sandwich:")
for sandwich in sandwich_orders:
    print(f"\t{sandwich}")
