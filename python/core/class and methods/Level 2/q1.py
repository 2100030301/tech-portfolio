"""
Q1. Create a class Student that:
•	Keeps track of the total number of students created.
•	Determines whether a student passed or failed based on a shared passing mark.
•	Provides a method to curve marks by increasing everyone’s marks by a percentage.
•	Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
Demonstrate:
1.	Creating multiple students.
2.	Applying a grading curve.
3.	Displaying updated results with letter grades.
"""

class Student:
    total_students = 0
    pass_mark = 35
    students_list = []
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1
        Student.students_list.append(self)
    def percentage(self):
        return f"{self.marks}%"
    @staticmethod
    def grade(marks):
        if marks > 85:
            return "A"
        elif marks > 70:
            return "B"
        elif marks > 55:
            return "C"
        elif marks > 40:
            return "D"
        elif marks >= 35:
            return "E"
        else:
            return "F"
    def is_pass(self):
        return self.marks >= Student.pass_mark
    @classmethod
    def apply_curve(cls, percent):
        for student in cls.students_list:
            student.marks += student.marks * percent / 100
            if student.marks > 100:
                student.marks = 100

s1 = Student("Rishi", 70)
s2 = Student("Sreya", 90)
s3 = Student("Valli", 33)
print(Student.total_students)
print()
for s in Student.students_list:
    print(s.name, "-", s.marks, "-", Student.grade(s.marks), "-", "Pass" if s.is_pass() else "Fail")
Student.apply_curve(10)
print()
for s in Student.students_list:
    print(s.name, "-", s.marks, "-", Student.grade(s.marks), "-", "Pass" if s.is_pass() else "Fail")