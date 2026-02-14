# 20. Write a program to sort a tuple of numbers.
tpl1 = (5,1,8,3,9,2)
print(sorted(tpl1))

# 21. Write a program to find the second largest element in a tuple.
tpl2 = list(set(tpl1))
tpl2.sort(reverse=True)
print("Second largest:", tpl2[1])

# 22. Write a program to remove duplicate values from a tuple.
tpl3 = (1,3,5,2,6,7,4,3,6,9,8)
tpl3 = tuple(set(tpl3))
print(tpl3)

# 23. Write a program to count how many times each element appears in a tuple.
tpl4 = (1, 2, 2, 3, 1, 4, 2)
freq = {}
for item in tpl4:
    freq[item] = freq.get(item, 0) + 1
print(freq)


# 24. Write a program to convert a list of tuples into a dictionary.
lst = [("a", 1), ("b", 2), ("c", 3)]
d = dict(lst)
print(d)


# 25 Write a program to find the common elements between two tuples.
tpl51 = (1, 2, 3, 4)
tpl62 = (3, 4, 5, 6)
common = tuple(set(tpl51) & set(tpl62))
print(common)
