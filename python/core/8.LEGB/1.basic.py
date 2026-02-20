# 1. Write a program demonstrating a local variable.
x = 10
def fun1():
    y=20 # local variable

# 2. Write a program demonstrating a global variable.
a = 5
def fun2():
    b = 8

# 3. Show that a local variable overrides a global variable.
k = 60
def fun3():
    k = 40
    print(k)
fun3()

# 4. Access a global variable inside a function.
t = 73
def fun4():
    t = 24
    print(t)
fun4()
print(t)

# 5. Modify a global variable inside a function using global.
h = 82
def fun5():
    global h
    h = 36
    print(h)
fun5()
print(h)