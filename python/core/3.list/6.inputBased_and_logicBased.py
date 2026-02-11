# 22. Take 5 numbers from the user, store them in a list, and print the list.
nums = []
for i in range(5):
    nums.append(int(input()))
print(nums)

# 23. Write a program to find the sum of all elements in a list
sum = 0
for i in nums:
    sum+=i
print(sum)

# 24. Write a program to find the maximum and minimum values in a list.
nums.sort()
print(nums[0],nums[-1],sep=",")

# 25. Write a program to remove all occurrences of a given value from a list.
value = 2
while value in nums:
    nums.remove(value)
print(nums)

# 26. Write a program to reverse a list without using reverse().
rev = []
for i in nums:
    rev.insert(0,i)
print(rev)