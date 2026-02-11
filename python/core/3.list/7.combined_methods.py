"""
27. Write a program to:
Take 5 numbers from the user
Store them in a list
Sort the list
Print the second largest number
"""
nums = []
for i in range(5):
    nums.append(int(input()))
nums.sort()
print(nums[-2])

"""
28. Write a program to:
Create a list of numbers
Copy it into another list
Clear the original list
Print both lists
"""
lst1 = [1,2,3,4,5,6]
lst2 = lst1.copy()
lst1.clear()
print(lst1,lst2)

# 29. Write a program to Count how many times each element appears in a list
values = [1,2,5,2,8,4,7,1,5,2,6]
for i in values:
    print(i,"-",values.count(i))


"""
30. Write a program to:
Merge two lists
Remove duplicates
Sort the final list
"""
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
merged = a + b
final = list(set(merged))
final.sort()
print(final)