"""
7. Use reduce() to concatenate a list of characters into a single string.
Example input: ['P', 'y', 't', 'h', 'o', 'n'].
"""

from functools import reduce
input = ['P', 'y', 't', 'h', 'o', 'n']
res = reduce(lambda x , y : x + y, input)
print(res)