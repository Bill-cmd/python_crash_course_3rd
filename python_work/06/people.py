person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

people = {
    'person1': {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
        'city': 'New York',
    },
    'person2': {
        'first_name': 'Natasha',
        'last_name': 'Doe',
        'age': 28,
        'city': 'Los Angeles',
    },
}

for person, person_info in people.items():
    print(f"\nPerson: {person}")
    full_name = f"{person_info['first_name'].title()} {person_info['last_name'].title()}"
    age = person_info['age']
    city = person_info['city']
    print(f"\tFull Name: {full_name}, Age: {age}, City: {city}")
    