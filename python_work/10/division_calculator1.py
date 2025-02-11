#import numbers

def is_number(value):
    """
    检查输入的字符串是否可以转换为数字。
    :param value: 输入的字符串
    :return: 如果可以转换为数字，返回 True;否则返回 False
    """
    try:
        int(value)
        return True
    except ValueError:
        return False

def get_input_number(prompt):
    """
    获取用户输入的数字或 'q'。
    :param prompt: 提示信息
    :return: 如果用户输入数字，返回该数字；如果用户输入 'q'，返回 'q'
    """
    while True:
        value = input(prompt)
        if value == 'q':
            return value
        elif is_number(value):
            return value
        else:
            print("Please enter a valid number or 'q' to quit.")


while True:
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")
    first_number = get_input_number("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = get_input_number("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    
    print(f"The answer is {answer}\n")
