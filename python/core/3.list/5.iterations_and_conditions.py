# 19. Write a program to print all elements of a list using a for loop
nums = [1,2,3,4,5,6,7,8,9]
for i in nums:
    print(i,end=" ")

print()

# 20. Write a program to print only the even numbers from a list
for i in nums:
    if i % 2 == 0:
        print(i,end=" ")

print()

# 21. Write a program to count how many numbers in a list are greater than 5
count=0
for i in nums:
    if i > 5:
        count+=1
print(count)