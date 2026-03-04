"""
Q4. Create a class Car with:
•	instance attribute mileage
•	class attribute wheels = 4
Add an instance method display_specs() that prints mileage and wheels.
Then change wheels using a class method, and print again.
"""

class Car:
    wheels=4
    def __init__(self,mileage):
        self.mileage=mileage
    def display_specs(self):
        print(self.mileage)
        print(Car.wheels)
    def change_wheels(cls,x):
        cls.wheels=x

c1=Car(120)
print(c1.wheels)
print(c1.mileage)
c1.change_wheels(6)
print(c1.wheels)