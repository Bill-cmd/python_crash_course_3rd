from pathlib import Path
import json

def is_number(value):
    """判断给定的值是否是整数"""
    try:
        int(value)
        return True
    except ValueError:
        return False
    

def get_user_input(prompt):
    """获取用户输入，并确保输入是一个整数"""
    while True:
        user_input = input(prompt)
        if is_number(user_input):
            return int(user_input)
        else:
            print("请输入一个整数。")


def save_favorite_number(path):
    """将用户的喜欢的数字保存到文件中"""
    path = Path('favorite_number.json')
    number = get_user_input("Please enter your favorite number: ")
    path.write_text(json.dumps(number))


def get_favorite_number(path):
    """从文件中获取用户的喜欢的数字"""
    if path.exists():
        number = json.loads(path.read_text(encoding='utf-8'))
        return number
    else:
        save_favorite_number(path)
        return get_favorite_number(path)

    
    
path = Path('favorite_number.json')

number = get_favorite_number(path)
print(f"Your favorite number is {number}.")


