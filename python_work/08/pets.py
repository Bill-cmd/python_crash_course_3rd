'''
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(animal_type='cat', pet_name='lucy')
'''
def describe_pet(pet_name, animal_type='dog'):
    '''显示宠物信息'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')
