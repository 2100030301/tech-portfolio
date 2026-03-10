"""
Q8. Create a class Course with:
•	class variable total_students
•	instance variable student_name
•	instance method enroll() → increments total_students
•	class method show_total(cls) → prints total students
•	static method is_eligible(age) → returns True if age ≥ 18
Demonstrate enrolling multiple students and show total count.
"""
from pickletools import read_unicodestring1


class Course:
    total_students=0
    def __init__(self,student_name):
        self.name=student_name
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18

c1 = Course("Rishi")
c1.enroll()
c2 = Course("Sreya")
c2.enroll()
c3 = Course("Valli")
c3.enroll()
c4 = Course("Sreeja")
c4.enroll()
print(Course.total_students)