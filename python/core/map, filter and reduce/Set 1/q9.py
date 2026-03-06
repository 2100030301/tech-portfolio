"""
9. Given a list of numbers:
[5, 10, 15, 20, 25, 30]
Perform the following in a single pipeline:
• Use map() to square each number
• Use filter() to keep only numbers divisible by 5
• Use reduce() to calculate the sum of remaining numbers
"""
from functools import reduce

lst = [5, 10, 7, 15, 3, 20, 25]
mp = list(map(lambda x : x*x, lst))
print(mp)
ft = list(filter(lambda x : x%5==0, mp))
print(ft)
rd = reduce(lambda x , y : x + y , ft)
print(rd)