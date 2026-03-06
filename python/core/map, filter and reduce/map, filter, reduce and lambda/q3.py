#  Use functools.reduce() with a lambda to find the largest number from a given list Dynamically.

k=list(map(int,input().split()))
from functools import reduce
print(reduce(lambda x,y: x if x>y else y,k))