"""
Q2. Design a class Product that:
•	Maintains a base tax rate applicable to all products.
•	Each product has a name and base price.
•	Has a method to compute final price including tax.
•	Can change tax rate for all products using one method.
•	Includes a function to check whether a given price is valid or not (non-negative and realistic).
Demonstrate:
1.	Creating multiple products.
2.	Changing the tax rate.
3.	Showing updated prices and validity checks.
"""

class Product:
    base_tax = 0.1
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def final_price(self):
        return self.price + (self.price * Product.base_tax)
    @classmethod
    def change_tax(cls, new_tax):
        cls.base_tax = new_tax
    @staticmethod
    def is_valid(price):
        return price >= 0 and price <= 100000

p1 = Product("Laptop", 50000)
p2 = Product("Phone", 20000)
p3 = Product("Headphones", -500)
print()
print(p1.name, p1.final_price())
print(p2.name, p2.final_price())
print()
print(Product.is_valid(p1.price))
print(Product.is_valid(p3.price))
Product.change_tax(0.2)
print()
print(p1.name, p1.final_price())
print(p2.name, p2.final_price())