# 6. Call a function using positional arguments.
def fun1(a,b):
    print(a+b)
fun1(4,7)

# 7. Call the same function using keyword arguments.
fun1(a=2,b=5)

# 8. Mix positional and keyword arguments correctly.
def greet(name, Bday):
    print(name, Bday)

greet("Rishi", Bday=20)

# 9. Write a program that causes an error due to incorrect argument order.
# greet(name="Ravi", 22)  # SyntaxError

# 10. Show what happens when a required argument is missing.
# fun1(5)  # TypeError: missing argument
