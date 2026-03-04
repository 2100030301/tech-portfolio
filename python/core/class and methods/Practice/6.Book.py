"""
Q6. Create a class Book with:
•	instance attributes title, author
•	a class variable total_books
•	a class method from_string(cls, book_str) that creates an object from "title-author" format
•	a static method is_valid_title(title) that checks if title has at least 3 characters
•	increment total_books for every book created
Demonstrate:
•	Creating books using both the constructor and the class method
•	Validating titles before creation
"""

class Book:
    total_books = 0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
        title,book=book_str.split("-")
        print("Book : " + title)
        print("Author : " + book)
    @staticmethod
    def is_valid_title(title):
        return len(title)>2

b1 = Book("wings of fire","A.P.J Abdhul Kalam")
b1.from_string("wings of fire-A.P.J Abdhul Kalam")
print(b1.is_valid_title(b1.title))
print(Book.total_books)
print()
b2 = Book("Geethanjali","Rabindhranath Tagoree")
b2.from_string("Geethanjali-Rabindhranath Tagoree")
print(b2.is_valid_title(b2.title))
print(Book.total_books)