# 1. Create a tuple with values 10, 20, 30, 40 and print it.
tpl1 = (1,2,3,4,5)
print(tpl1)

# 2. Write a program to access the first, last, and third elements of a tuple.
print(tpl1[0],tpl1[1],tpl1[2])

# 3. Create a tuple with one element and print its type.
tpl2 = (7,)
print(type(tpl2))

# 4. Write a program to find the length of a tuple.
print(len(tpl1))
print(len(tpl2))

# 5. Given a tuple t = (5, 10, 15, 20), print all elements using a loop.
tpl3 = (5,10,15,20)
for i in tpl3:
    print(i,end=" ")
