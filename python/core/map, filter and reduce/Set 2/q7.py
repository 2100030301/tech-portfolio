"""
Q7. Build an Inventory class that:
•	Tracks the total number of items across all inventories.
•	Each instance maintains its own stock dictionary ({"item": quantity}).
•	Provides a method to add or remove stock.
•	Allows updating a minimum stock threshold globally.
•	Offers a static checker to verify if a stock level is below threshold.
Demonstrate:
1.	Managing multiple inventories.
2.	Adjusting stock threshold.
3.	Using static validation inside the instance logic.
"""

class Inventory:
    total_items = 0
    min_threshold = 5
    def __init__(self):
        self.stock = {}
    def update_stock(self, item, qty):
        if item in self.stock:
            self.stock[item] += qty
        else:
            self.stock[item] = qty
        Inventory.total_items += qty
    @classmethod
    def update_threshold(cls, new_threshold):
        cls.min_threshold = new_threshold
    @staticmethod
    def below_threshold(quantity):
        return quantity < Inventory.min_threshold

i1 = Inventory()
i2 = Inventory()
i1.update_stock("Pen", 10)
i1.update_stock("Notebook", 3)
i2.update_stock("Pencil", 2)
print(i1.stock)
print(i2.stock)
Inventory.update_threshold(4)
print("Pen low:", Inventory.below_threshold(i1.stock["Pen"]))
print("Notebook low:", Inventory.below_threshold(i1.stock["Notebook"]))