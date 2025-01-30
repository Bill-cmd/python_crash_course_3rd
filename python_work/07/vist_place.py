prompt_name = "What's your name? "
prompt_place = "If you could visit one place in the world, where would you go? "
responses = {}

polling_active = True

while polling_active:
    name = input(prompt_name)
    place = input(prompt_place)

    responses[name] = place
    repeat = input("Would you like to let another respond (yes/no)? ")
    if repeat.lower() == 'no':
        polling_active = False

for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
