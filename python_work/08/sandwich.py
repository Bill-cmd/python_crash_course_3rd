def make_sandwich(*toppings):
    print("Your sandwich has been made by:")
    for topping in toppings:
        print(f"\t- {topping}")

make_sandwich("Wather", "rock", "sand")