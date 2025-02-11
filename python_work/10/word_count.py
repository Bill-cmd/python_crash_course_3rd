from pathlib import Path

def count_words(path):
    """计算一个文件中大致包含多少个单词。"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        """
        如果静默错误，即什么都不做，这里可以放置 pass
        pass
        """
    else:
        words = contents.split()
        num_words = len(words)
        words_set = set(words)
        num_words_set = len(words_set)
        """
        nums = {
            'num_words': num_words,
            'num_words_set': num_words_set
        }

        return nums
        """
        print(f"The file {path.name} has about {num_words} words, and {num_words_set} distinct words.")

"""
path = Path('alice.txt')
count_words(path)
"""
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

