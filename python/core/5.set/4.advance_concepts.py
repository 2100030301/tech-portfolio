# 16. Convert a list into a set to remove duplicates.
lst1 = [1,5,3,7,6,4,9,7,3,1,6,2,8]
st1 = set(lst1)
print(st1)

# 17. Convert a set into a tuple.
st2 = {1,2,3,4,5,6}
tpl1 = tuple(st2)
print(tpl1)

# 18. Check if an element exists in a set.
print(5 in st2)

# 19. Find maximum and minimum elements in a numeric set.
print("Max :", max(st1))
print("Min :", min(st2))

# 20. Count frequency of elements in a list using set logic.
lst2 = [1, 2, 2, 3, 1, 4]
for i in set(lst2):
    print(i, ":", lst2.count(i))
