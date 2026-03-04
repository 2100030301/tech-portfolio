# 1. Write a lambda function to add two numbers.
add = lambda x,y : x+y
print(add(7,8))

# 2. Write a lambda function to find square of a number.
square = lambda x : x*x
print(square(8))

# 3. Write a lambda function to check if a number is even.
even = lambda x : x%2==0
print(even(4))

# 4. Write a lambda function to return the maximum of two numbers.
max = lambda x,y : x if x>y else y
print(max(2,5))

# 5. Store a lambda function in a variable and call it.
name = lambda x : "Hello!" + x
print(name("Rishi"))