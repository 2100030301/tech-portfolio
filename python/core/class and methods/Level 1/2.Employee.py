"""
Q2. Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances
"""

class Employee:
    company_name="TechCorp"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_company(cls,new_name):
        cls.company_name = new_name

e1 = Employee("Rishi")
e1.change_company("CvCorp")
print(e1.company_name)