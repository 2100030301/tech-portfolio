"""
3. Use functools.reduce() with a lambda to find the largest number from a given
list Dynamically.
"""

from functools import reduce
lst = [14, 2, 73, 673, 98, 532, 6, 892]
res = reduce(lambda x , y : x if x>y else y, lst)
print(res)