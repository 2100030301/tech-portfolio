st1 = {1,2,3,4,5}
st2 = {2,4,6,8}
st3 = {1,3,5}

# 11. Find union of two sets.
print(st1 | st2)

# 12. Find intersection of two sets.
print(st1 & st3)

# 13. Find difference between two sets.
print(st1 - st2)

# 14. Find symmetric difference.
print(st1 ^ st3)

# 15. Check whether one set is a subset of another.
print(st3.issubset(st1))