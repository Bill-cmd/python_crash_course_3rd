from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip()

#print(contents)

file_content = []

for line in contents.splitlines():
    line = line.replace('Python', 'C')
    file_content.append(line)

print("=======================================================")

for line in file_content:
    print(line)

print(len(file_content))

print(type(file_content))

