"""
Q2. Create a class Employee with attributes name and company_name = "TechCorp".
Add a class method change_company(cls, new_name) to update the company name for all employees.
Demonstrate how this change affects all instances
"""

class Employee:
    company_name="TechCorp"
    @classmethod
    def changename(cls,x):
        cls.company_name=x

print(Employee.company_name)
Employee.company_name="CVCORP"
print(Employee.company_name)