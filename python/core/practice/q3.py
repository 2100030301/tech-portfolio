from functools import reduce
# 3. Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.
lst = [1,2,3,4,5]
y = lambda a,b : a>b
def fun1(a,b):
        if a > b:
            return a
        else:
            return b
l1=reduce(y(lst))
print(l1)

