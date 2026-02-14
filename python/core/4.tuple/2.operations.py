# 6. Write a program to concatenate two tuples.
tpl1 = (1,3,5,7,9)
tpl2 = (2,4,6,8,10)
print(tpl1+tpl2)

# 7. Write a program to repeat a tuple 3 times.
print(tpl1 * 3)

# 8. Write a program to check whether an element exists in a tuple.
x = 7
if x in tpl2:
    print("Yes")
else:
    print("No")

# 9. Write a program to find the index of an element in a tuple.
print(tpl1.index(3))

# 10. Write a program to find the maximum and minimum values in a numeric tuple.
print("Min :", min(tpl2))
print("Max :", max(tpl1))