# 17. Write a program to pack multiple values into a tuple and unpack them into variables.
a,b,c = 10,20,30
t = a,b,c
print(t)

# 18. Write a program to swap two variables using tuple unpacking.
a = 10
b = 20
a , b = b , a
print(a,b)

# 19. Write a program to unpack only the first two values from a tuple.
t = (1,2,3,4,5)
a,b,*rest = t
print(a,b)
print(*rest)