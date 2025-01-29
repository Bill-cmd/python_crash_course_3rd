'''
age = input("How old are you? ")
try:
    age = int(age)
    print(age)
except ValueError:
    print("Please enter a number.")
'''

while True:
    age = input("How old are you? ")
    try:
        age = int(age)
        print(age)
        break
    except ValueError:
        print("Please enter a number. Try again.")

