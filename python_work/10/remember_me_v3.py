from pathlib import Path
import json

def get_stored_username(path):
    """如果存储了用户名，就获取它"""
    if path.exists():
        content = path.read_text()
        return json.loads(content)


def get_new_username(path):
    """提示用户输入用户名"""
    username = input("What is your name? ")
    return path.write_text(json.dumps(username))


def greet_user(path):
    """问候用户，并指出其名字"""
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}")

path = Path('username.json')
greet_user(path)

