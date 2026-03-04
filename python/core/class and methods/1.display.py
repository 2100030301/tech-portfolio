"""
Create a class Student with:
Attributes: name, marks
A method display() that prints both values.
Create one object and call the method.
"""

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(self.name,end=" ")
        print(self.marks)

s1=Student("Rishi",90)
s1.display()
s2=Student("Sreya",95)
s2.display()