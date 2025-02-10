from pathlib import Path


# 定义一个函数，用于读取文件内容
def read_file(file_path):
    # 将文件路径转换为Path对象
    path = Path(file_path)
    try:
        # 尝试读取文件内容，编码格式为utf-8
        content = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # 静默错误信息
        pass
    else:
        # 如果文件存在，打印文件内容
        print(content)

print("==============================================================")
read_file('cats.txt')
read_file('dogs.txt')
read_file('pigs.txt')

'''
path_cats = Path('cats.txt')
path_dogs = Path('dogs.txt')

try:
    content_cats = path_cats.read_text(encoding='utf-8')
except FileNotFoundError:
    print("Sorry, the file cats.txt was not found.")
else:
    print(content_cats)

try:
    content_dogs = path_dogs.read_text(encoding='utf-8')
except FileNotFoundError:
    print("Sorry, the file dogs.txt was not found.")
else:
    print(content_dogs)
'''