# 1.  Use map() with a lambda to add 5 to every element of the following nested list [[1, 2], [3, 4], [5, 6]]

import fun
from functools import reduce



# 2. Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use filter() to keep only the keys whose values are greater than 50

d = {"apple": 100, "banana": 40, "cherry": 150}
def fun(a) :
    if d[a]>50:
        return True
    return False
d1 = list(filter(fun,d))
print(d1)

# 3. Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.
lst = [1,2,3,4,5]
def fun1(a):
    for i in a-1:
        return a[i] > a[i+1]
l1=reduce(fun1,lst)
print(l1)