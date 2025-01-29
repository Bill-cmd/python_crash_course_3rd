string1 = "This is a string"
string2 = "This Is a string"
print(f"{string1} == {string2}")
print(string1 == string2)
print(f"{string1} != {string2}")
print(string1 != string2)
print(f"string1.lower() == string2.lower()")
print(string1.lower() == string2.lower())

number1 = 10
number2 = 20

print(f"{number1} == {number2}: {number1 == number2}")
print(f"{number1} != {number2}: {number1 != number2}")
print(f"{number1} > {number2}: {number1 > number2}")
print(f"{number1} < {number2}: {number1 < number2}")

list1 = [1, 2, 3]
number1 = 2
number2 = 4

print(f"{number1} in {list1}: {number1 in list1}")
print(f"{number2} not in {list1}: {number2 not in list1}")

print(f"{number1} in {list1} and {number2} not in {list1}: {number1 in list1 and number2 not in list1}")
