# 21. Find common elements between two lists using sets.
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
print(set(lst1) & set(lst2))

# 22. Remove duplicates from a string using sets.
str = "Rishitha"
st1 = set(str)
print(st1)

# 23. Check if two sets are disjoint.
st2 = {1, 2}
st3 = {3, 4}
print(st2.isdisjoint(st3))

# 24. Find elements present in either set but not both.
st4 = {1, 2, 3}
st5 = {3, 4, 5}
print(st4 ^ st5)

# 25. Create a program that takes user input and stores unique values only.
val = set()
for i in range(5):
    num = int(input())
    val.add(num)
print(val)
