from functools import reduce

lst = [1, 2, 6, 5, 2, 3, 8, 9, 12]
rd = reduce(lambda x, y: x+y, list(filter(lambda x : x%7==0, list(map(lambda x : x**3, lst)))), list(map(lambda x : x**3, lst)))
print(rd)