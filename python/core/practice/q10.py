"""
10.  Given a list of numbers:
[5, 10, 15, 20, 25, 30]
Perform the following in a single pipeline:
• Use map() to square each number
• Use filter() to keep only numbers divisible by 5
• Use reduce() to calculate the sum of remaining number
"""
from functools import reduce

def fun1 (a):
    return a**2
l = [5,10,15,20,25,30]
l1 = list(map(fun1,l))
print(l1)

def fun2 (a):
    return a%5==0
l2 = list(filter(fun2,l))
print(l2)

def fun3 (a):
    return l[a]+l[a+1]
l3 = reduce(fun3,l)