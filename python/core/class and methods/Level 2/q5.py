"""
Q5. Create a class Course that:
•	Tracks total courses created.
•	Each course has a title, duration, and enrolled_students.
•	Provides a method to enroll a new student.
•	Allows updating the minimum duration for a valid course across all instances.
•	Has a static function to check if a given duration is realistic (not negative, not too large).
Demonstrate:
1.	Creating multiple courses.
2.	Enrolling students.
3.	Updating minimum duration and checking durations.
"""

class Course:
    total_courses = 0
    min_duration = 1
    def __init__(self, title, duration, enrolled_students=0):
        self.title = title
        self.duration = duration
        self.enrolled_students = enrolled_students
        Course.total_courses += 1
    def enroll_student(self):
        self.enrolled_students += 1
    @classmethod
    def update_min_duration(cls, new_duration):
        cls.min_duration = new_duration
    @staticmethod
    def is_valid_duration(duration):
        return duration >= 0 and duration <= 1000

c1 = Course("Python", 40)
c2 = Course("Java", 60)
c1.enroll_student()
c1.enroll_student()
c2.enroll_student()
print(c1.enrolled_students)
print(c2.enrolled_students)
Course.update_min_duration(10)
print(Course.is_valid_duration(40))
print(Course.is_valid_duration(-5))