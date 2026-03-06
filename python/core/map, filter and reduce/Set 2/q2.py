"""
2. Given two lists:
a = [1, 2, 3, 4] b = [10, 20, 30, 40]
Use map() with a lambda to create a new list containing the sum of corresponding
elements.
What happens if the lists are of unequal length?
"""

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
res = list(map(lambda x , y : x + y, a ,b))
print(res)

a = [1, 2, 3, 4]
b = [10, 20, 30]
res = list(map(lambda x , y : x + y, a ,b))
print(res)