import timeit

lst = [2, 5, 6, 7, 8, 9, 2, 9, 9]
lst.reverse()
print(lst)
lst = lst[::-1]
print(lst)

'''
lst1 = list(range(1000000))
time_slice = timeit.timeit(lambda: lst[::-1], number=1000)

time_reverse = timeit.timeit(lambda: lst.copy().reverse(), number=1000)

print(f"Time for slice: {time_slice}")
print(f"Time for reverse: {time_reverse}")
'''

string = "Hello, World!"
print(string[::-1])

print(sum(lst) / len(lst))
print(sum(lst)/float(len(lst)))
print(lst.count(9))
