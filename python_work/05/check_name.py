current_users = ['bill', 'StEve', 'elon', 'admin', 'Jeff']
new_users = ['bill', 'natasha', 'elON', 'musk', 'Barack']

current_users_lower = [name.lower() for name in current_users]

for name in new_users:
    if name.lower() in current_users_lower:
        print(f"{name} is already taken. Please enter a new username.")
    else:
        print(f"{name} is available.")

