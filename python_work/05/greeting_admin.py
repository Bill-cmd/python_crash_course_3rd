lst = ['bill', 'StEve', 'elon', 'admin', 'Jeff']
lst1 = []

if not lst1:
    print("We need to find some users!")
else:
    for name in lst:
        if name == 'admin':
            print(f"Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {name.title()}, thank you for logging in again.")
