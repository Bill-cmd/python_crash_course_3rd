sandwich_orders = ['Bacon', 'Bagel toast', 'Crisp']
finished_sandwich = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)

print(f"\nThe list of sandwich:")
for sandwich in finished_sandwich:
    print(f"\t{sandwich}")
