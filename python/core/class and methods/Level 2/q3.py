"""
Q3. Create an Employee class that:
•	Keeps a minimum experience required for promotion (shared across all employees).
•	Stores employee name, experience, and department.
•	Has a method to check eligibility for promotion.
•	Provides a function to update promotion criteria globally.
•	Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
Demonstrate:
1.	Creating employees from different departments.
2.	Changing promotion criteria.
3.	Displaying eligibility results and department validation.
"""

class Employee:
    min_exp = 2   # minimum experience required for promotion
    def __init__(self, name, experience, department):
        self.name = name
        self.experience = experience
        self.department = department
    def is_eligible(self):
        return self.experience >= Employee.min_exp
    @classmethod
    def update_promotion_criteria(cls, new_exp):
        cls.min_exp = new_exp
    @staticmethod
    def is_valid_department(dept):
        return dept in ["HR", "Tech", "Admin"]

e1 = Employee("Rishi", 5, "Tech")
e2 = Employee("Valli", 7, "HR")
e3 = Employee("Sreya", 1, "Admin")
print(e1.department, Employee.is_valid_department(e1.department))
print(e2.department, Employee.is_valid_department(e2.department))
print()
print(e1.name, e1.is_eligible())
print(e3.name, e3.is_eligible())
Employee.update_promotion_criteria(6)
print()
print(e1.name, e1.is_eligible())
print(e2.name, e2.is_eligible())