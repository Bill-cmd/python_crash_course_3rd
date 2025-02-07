from random import randint

class Die():
    def __init__(self):
        self.sides = 6

    def roll_die():
        return randint(1, 6)

class Die10():
    """A die with 10 sides"""
    def __init__(self):
        self.sides = 10

    def roll_die():
        return randint(1, 10)

class Die20():
    """A die with 20 sides"""
    def __init__(self):
        self.sides = 20

    def roll_die():
        return randint(1, 20)


i = 6
print("===A die with 6 sides===")
while i > 0:
    print(Die.roll_die())
    i -= 1

i = 10
print("===A die with 10 sides===")
while i > 0:
    print(Die10.roll_die())
    i -= 1

i = 10
print("===A die with 20 sides===")
while i > 0:
    print(Die20.roll_die())
    i -= 1
