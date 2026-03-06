# Use filter() to remove all vowels from a string and print the final string.

nv = "aeiouAEIOU"
st = list(filter(lambda x: x not in nv,input()))
print(st)