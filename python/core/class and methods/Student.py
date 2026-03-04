class Student:
    batch="Python"
    def __init__(self,name):
        self.name=name
    def change_batch(self,bname):
        self.bname=bname
    @classmethod
    def change_batchname(cls,batchname):
        cls.batch = batchname

s1=Student("Rishi")
print(s1.name)
print(s1.batch)
Student.change_batchname("py-06")
print(s1.batch)