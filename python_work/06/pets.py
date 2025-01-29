pets = {
    'dog': {
        'name': 'Buddy',
        'owner': 'John',
        'age': 5,
    },
    'cat': {
        'name': 'Whiskers',
        'owner': 'Natasha',
        'age': 3,
    },
    'parrot': {
        'name': 'Polly',
        'owner': 'John',
        'age': 2,
    },
}

for pet, pet_info in pets.items():
    print(f"\nPet: {pet}")
    name = pet_info['name']
    owner = pet_info['owner']
    age = pet_info['age']
    print(f"\tName: {name}, Owner: {owner}, Age: {age}")

