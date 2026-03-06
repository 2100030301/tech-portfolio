"""
6. Use filter() to remove all vowels from a string and print the final string.
"""

str = "LaghuvarapuLaxmiRishita"
nv = "aeiouAEIOU"
res = list(filter(lambda x : x not in nv, str))
print(res)