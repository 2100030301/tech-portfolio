"""
Q9. Design a LibraryMember class that:
•	Tracks total active members.
•	Each member has a name and books_borrowed count.
•	Has a function to borrow books, with borrowing limit common to all.
•	Allows updating borrowing limit globally.
•	Has a static function to check if book title is valid (non-empty string, reasonable length).
Demonstrate:
1.	Borrowing books for multiple users.
2.	Changing borrowing limits.
3.	Validating book titles before borrowing.
"""

class LibraryMember:
    total_members = 0
    borrow_limit = 7
    def __init__(self, name, books_borrowed):
        self.name = name
        self.books_borrowed = books_borrowed
        LibraryMember.total_members += 1
    def limit(self, books):
        if books + self.books_borrowed <= LibraryMember.borrow_limit:
            self.books_borrowed += books
            return True
        return False
    @classmethod
    def update_limit(cls, new_limit):
        cls.borrow_limit = new_limit
    @staticmethod
    def is_valid(book_name):
        return isinstance(book_name, str) and 0 < len(book_name) <= 100

l1 = LibraryMember("Rishi", 6)
l2 = LibraryMember("Valli", 2)
print(l1.limit(2))
print(l2.limit(3))
LibraryMember.update_limit(10)
print(l1.limit(2))
print(LibraryMember.is_valid("Python Basics"))
print(LibraryMember.is_valid(""))