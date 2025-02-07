from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip()

print(contents)

file_content = []

for line in contents.splitlines():
    file_content.append(line)

print("=======================================================")

print(file_content)
print(len(file_content))

print(type(file_content))

