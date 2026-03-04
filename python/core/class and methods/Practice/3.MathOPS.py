"""
Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
Then call it both from the class and an instance.
"""

class MathOps:
    def __init__(self,x):
        self.x=x
    @staticmethod
    def is_even(x):
        if x%2:
            return "Odd"
        else:
            return "Even"

n1=MathOps(7)
print(n1.is_even(n1.x))
print(MathOps.is_even(10))