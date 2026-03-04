"""
Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed.
"""

class Student:
    clg="KLU"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        if self.marks>40:
            return "Pass"
        else:
            return "Fail"

print(Student.clg)
Student.clg="KL Univeristy"
print(Student.clg)
p1=Student("Rishi",90)
print(p1.is_passed())
p2=Student("Sreya",35)
print(p2.is_passed())