"""
Q1. Create a class Student with instance attributes name and marks.
Add an instance method is_passed() that returns True if marks > 40.
Then create 2 student objects and print whether each has passed or failed.
"""

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_passed(self):
        return self.marks > 40

s1 = Student("Rishi",90)
print(s1.is_passed())
s2 = Student("Valli",35)
print(s2.is_passed())
