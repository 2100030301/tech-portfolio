# 21. Write a calculator function using parameters.
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b

print(calc(10, 5, '+'))

# 22. Write a function that checks if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))

# 23. Write a function that accepts any number of student marks and returns average.
def average(*marks):
    return sum(marks) / len(marks)

print(average(80, 90, 70))

# 24. Write a function that swaps two numbers using parameters.
def swap(a, b):
    return b, a

x, y = swap(5, 10)
print(x, y)

# 25. Create a function that modifies a list passed as argument.
def modify(lst):
    lst.append(100)

numbers = [1, 2, 3]
modify(numbers)
print(numbers)