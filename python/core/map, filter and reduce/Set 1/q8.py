"""
8. Given a list of integers, use map() with id() to print the memory address
of each element. Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.
"""

lst = [10, 350, 10, 350, 20]
res = list(map(lambda x : id(x) , lst))
print(res)