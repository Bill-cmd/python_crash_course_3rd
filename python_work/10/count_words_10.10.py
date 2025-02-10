from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print('Sorry, the file does not exist.')
else:
    word_without_space = content.lower().count('the')
    word_with_space = content.lower().count('the ')
    print(f"{word_without_space} 'the' in the file.")
    print(f"{word_with_space} 'the ' in the file.")
    print(f"The difference is {word_without_space - word_with_space}.")
    