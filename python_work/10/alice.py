from pathlib import Path

path = Path('alice.txt')
try:
    content = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # 计算文件大致包含多少个单词
    words = content.split()
    num_words = len(words)
    words_set = set(words)
    num_words_set = len(words_set)
    print(f"The file {path} has about {num_words} words.")
    print(f"The set has about {num_words_set} words.")

