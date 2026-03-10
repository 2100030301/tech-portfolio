"""
Q4. Build a Loan class that:
•	Has a common interest rate for all loans.
•	Each object stores borrower name and principal.
•	Calculates total payable amount.
•	Provides a function to update the interest rate.
•	Provides a static function to check loan eligibility (e.g., salary > certain threshold).
Demonstrate:
1.	Creating multiple loan accounts.
2.	Updating interest rates.
3.	Checking eligibility and total repayment for borrowers.
"""

class Loan:
    interest_rate = 5   # 5% interest
    def __init__(self, name, principal):
        self.name = name
        self.principal = principal
    def total_payable(self):
        return self.principal + (self.principal * Loan.interest_rate / 100)
    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
    @staticmethod
    def check_eligibility(salary):
        return salary >= 30000

l1 = Loan("Rishi", 100000)
l2 = Loan("Valli", 200000)
print()
print(l1.name, l1.total_payable())
print(l2.name, l2.total_payable())
print()
print("Salary 25000:", Loan.check_eligibility(25000))
print("Salary 50000:", Loan.check_eligibility(50000))
Loan.update_interest_rate(7)
print()
print(l1.name, l1.total_payable())
print(l2.name, l2.total_payable())