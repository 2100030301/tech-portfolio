# Use reduce() to concatenate a list of characters into a single string. Example input: ['P', 'y', 't', 'h', 'o', 'n'].
from functools import reduce
l = ['P', 'y', 't', 'h', 'o', 'n']
st = reduce(lambda x,y:x+y,l)
print(st)