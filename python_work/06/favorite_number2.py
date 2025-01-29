'''
favorite_numbers = {
    'jen': 7,
    'sarah': 3,
    'edward': 9,
    'phil': 2,
}

print(f"Jen's favorite number is {favorite_numbers['jen']}.")
print(f"Sarah's favorite number is {favorite_numbers['sarah']}.")
print(f"Edward's favorite number is {favorite_numbers['edward']}.")
print(f"Phil's favorite number is {favorite_numbers['phil']}.")
'''
favorite_numbers = {
    'jen': [7, 8],
    'sarah': [3, 4],
    'NTASHA': [5],
    'edward': [9, 10],
    'phil': [2, 3],
    'bILL': [],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) == 0:
        print(f"\n{name.title()} has no favorite numbers.")
    elif len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is {numbers[0]}.")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")
