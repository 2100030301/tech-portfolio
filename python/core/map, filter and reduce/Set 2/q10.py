"""
Q10. Create a class Member that:
•	Has a shared BMI limit for “fit” status.
•	Each member stores name, height, weight.
•	Has a method to calculate BMI and check fit status.
•	Provides a function to update BMI limit for all members.
•	Offers a tool to check if height and weight entered are valid numbers.
Demonstrate:
1.	Creating multiple members.
2.	Updating BMI standard.
3.	Displaying fit status and input validity.
"""

class Member:
    bmi_limit = 25
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def bmi(self):
        return self.weight / (self.height ** 2)
    def fit_status(self):
        return self.bmi() <= Member.bmi_limit
    @classmethod
    def update_bmi_limit(cls, new_limit):
        cls.bmi_limit = new_limit
    @staticmethod
    def valid_input(height, weight):
        return isinstance(height, (int, float)) and isinstance(weight, (int, float)) and height > 0 and weight > 0

p1 = Member("Rishi", 1.75, 70)
p2 = Member("Valli", 1.60, 80)
print(p1.bmi())
print(p1.fit_status())
print(p2.bmi())
print(p2.fit_status())
Member.update_bmi_limit(24)
print()
print(p1.fit_status())
print(Member.valid_input(1.7, 65))
print(Member.valid_input(-1.7, 65))