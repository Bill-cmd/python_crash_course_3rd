from pathlib import Path

path = Path('D:\\git\\python_crash_course_3rd\\python_work\\10\\pi_million_digits.txt')

contents = path.read_text().rstrip()

pi_string = ''

for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

