def is_number(number):
    """Check if the input is an number."""
    try:
        int(number)
        return True
    except ValueError:
        return False
    
def get_input_number(prompt):
    while True:
        user_input_value = input(prompt)
        if user_input_value == 'q':
            return user_input_value
        elif is_number(user_input_value):
            return int(user_input_value)
        else:
            print("Please enter a valid number.")

while True:
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")

    first_number = get_input_number("First number: ")
    if first_number == 'q':
        print("Goodbye!")
        break

    second_number = get_input_number("Second number: ")
    if second_number == 0:
        print("Goodbye!")
        break
    
    print(f"{first_number} + {second_number} = {first_number + second_number}\n")


