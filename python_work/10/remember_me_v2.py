from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    content = path.read_text()
    username = json.loads(content)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    content = json.dumps(username)
    path.write_text(content)
    print(f"We'll remember you when you come back, {username}")
