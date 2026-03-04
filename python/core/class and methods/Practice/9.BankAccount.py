"""
Q9. Create a class BankAccount with:
•	class variable bank_name
•	instance variables holder and balance
•	instance method deposit(amount)
•	class method change_bank_name(cls, new_name)
•	static method validate_amount(amount) → returns True if amount > 0
Show transactions and how static + class methods work together.
"""

class BankAccount:
    bank_name="ICICI"
    def __init__(self,holder,balance):
        self.holder=holder
        self.balance=balance
    def deposit(self,amt):
        self.balance= amt + self.balance
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
    @staticmethod
    def validate_amount(amt):
        return amt>0

b1 = BankAccount("Rishi",100000)
b1.deposit(70000)
b1.change_bank_name("SBI")
print(BankAccount.bank_name)
print(b1.validate_amount(b1.balance))
print(b1.balance)