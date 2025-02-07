from pathlib import Path

path = Path('D:\\git\\python_crash_course_3rd\\python_work\\10\\pi_million_digits.txt')

contents = path.read_text().rstrip()

pi_string = ''

for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string[:52])
print(len(pi_string))
