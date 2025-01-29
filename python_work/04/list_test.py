lst = [1,2,3,4,5]

# 求列表的从长度
print(len(lst))
# 判断6是否在列表中
print(6 in lst)
print(f"{lst + [6, 7, 8]}")
print(f"{lst * 2}")
print(f"{max(lst)}")
print(f"{min(lst)}")
print(f"{sum(lst)}")
lst.insert(1, 10)
print(lst)
lst.append(11)
print(lst)

print(id(lst))

