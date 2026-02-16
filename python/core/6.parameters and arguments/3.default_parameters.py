# 11. Write a function with a default parameter.
def fun1(name="Rishi"):
    print("Hello",name)
fun1()

# 12. Call the function with and without passing the default value.
fun1("Laxmi")

# 13. Write a function with multiple default parameters.
def fun2(name, Bday=20, city="Miryalaguda"):
    print(name, Bday, city)
fun2("Rishi")

# 14. Show that default parameters must come after non-default parameters.
# def test(a=10, b):  # SyntaxError
#     pass

# 15. Demonstrate a mutable default argument problem.
def add_item(item, lst=[]):
    lst.append(item)
    return lst
print(add_item(1))
print(add_item(2))  # Unexpected behavior
