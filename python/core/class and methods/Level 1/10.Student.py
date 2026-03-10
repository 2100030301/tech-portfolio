"""
Q10. Create a class Student with:
•	class variable passing_marks = 40
•	instance attributes name, marks
•	instance method result() → prints pass/fail using class variable
•	class method update_passing_marks(cls, new_marks)
•	static method grade_category(marks) → returns "A", "B", "C" based on score ranges
Use all three in a program that:
1.	Creates students
2.	Updates the passing criteria
3.	Displays grade category and result
"""

class Student:
    passing_mark=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks > Student.passing_mark:
            return True
        return False
    @classmethod
    def update_passing_marks(cls,marks):
        cls.passing_mark=marks
        return cls.passing_mark
    @staticmethod
    def grade_category(marks):
        if marks>85:
            print("A")
        elif marks>70:
            print("B")
        elif marks>65:
            print("C")
        elif marks<Student.passing_mark:
            print("Fail")
        else:
            print("D")

s2=Student("Rishi",33)
s2.grade_category(s2.marks)
Student.update_passing_marks(20)
s2.grade_category(s2.marks)