from pathlib import Path

# 使用相对路径：
# path = Path('pi_digits.txt')
# 使用绝对路径, 路径要使用/或\\代替windows路径中的\：
path = Path('D:\\git\\python_crash_course_3rd\\python_work\\10\\pi_digits.txt')
contents = path.read_text()
# 删除行尾的换行符
# 方法链式调用：
# contents = path.read_text().rstrip()
contents = contents.rstrip()

lines = contents.splitlines()
for line in lines:
    print(line)

print('---')
print(contents)


