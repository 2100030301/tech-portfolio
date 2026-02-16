# 16. Write a function using *args to accept multiple numbers and return their sum.
def fun1(*numbers):
    print(sum(numbers))
print(fun1(1, 2, 3, 4))

# 17. Write a function using **kwargs to print key-value pairs.
def fun2(**data):
    for key, value in data.items():
        print(key, value)
fun2(name="Rishi", Bday=20)

# 18. Combine positional, default, *args, and **kwargs in one function.
def fun3(a, b=10, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)
fun3(5, 20, 1, 2, x=100)

# 19. Unpack a tuple while calling a function.
def fun4(a, b):
    print(a + b)
values = (3, 4)
fun4(*values)

# 20. Unpack a dictionary while calling a function.
def person(name, Bday):
    print(name, Bday)

data = {"name": "Rishi", "Bday": 20}
person(**data)
