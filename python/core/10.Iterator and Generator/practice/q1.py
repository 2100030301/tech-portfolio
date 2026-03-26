"""
1. Write a custom iterator that prints numbers from 1 to N.
"""

class A:
    def __init__(self, n):
        self.i=0
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if self.i>self.n-1:
            raise StopIteration
        else:
            self.i+=1
            return self.i
p1=A(10)
for i in p1:
    print(i)