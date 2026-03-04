# 1. Use map() to double all numbers in a list.
lst1 = [1,2,3,4,5]
mp1 = list(map(lambda x : x * 2,lst1))
print(mp1)

# 2. Use map() to find square of numbers.
lst2 = [6,7,8,9,10]
mp2 = list(map(lambda x : x * x,lst2))
print(mp2)

# 3. Convert list of integers to strings using map().
lst3 = [2,4,6,8]
mp3 = list(map(str,lst3))
print(mp3)

# 4. Convert list of strings to integers using map().
lst4 = ["1","3","5","7","9"]
mp4 = list(map(int,lst4))
print(mp4)

# 5. Use map() with a normal function (not lambda).
def fun1(x):
    return x * 5
lst5 = [2,7,3,1,9,4]
mp5 = list(map(fun1,lst5))
print(mp5)