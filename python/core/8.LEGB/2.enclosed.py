# 6. Write a nested function showing enclosing scope.
def outer():
    x = 10
    def inner():
        print(x)
    inner()
outer()

# 7. Modify enclosing variable using nonlocal.
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)
outer()

# 8. Show error when modifying enclosing variable without nonlocal.
def outer():
    x = 10
    def inner():
        # x = 20  # Treated as local
        print(x)
    inner()
outer()

# 9. Demonstrate LEGB lookup order.
x = "Global"
def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print(x)
    inner()
outer()

# 10. Create three variables with same name in different scopes and print resolution.
x = "Global"
def outer():
    x = "Enclosing"
    def inner():
        print(x)
    inner()
outer()