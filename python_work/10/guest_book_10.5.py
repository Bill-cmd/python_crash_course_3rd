from pathlib import Path

guest_book_file = Path("guest_book.txt")
names = ''

while True:
    name = input("Enter your name: ")
    if name.lower() == 'q':
        break
    else:
        names += name + '\n'

print(names)
guest_book_file.write_text(names.strip())
