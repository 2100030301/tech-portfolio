"""
4. What happens if the lambda passed to reduce() accepts only one parameter or
three parameters? Explain the output or error.
"""
from logging import logMultiprocessing

"""
reduce should only have 2 parameters 
"""

from functools import reduce

lst = [2, 5, 3, 6, 1, 8,]

rd1 = reduce(lambda x : x + 10)
print(rd1) # TypeError: reduce() takes at least 2 positional arguments (1 given)

rd2 = reduce(lambda x , y , z : x + y + z)
print(rd2)