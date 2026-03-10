class Book:
    total_books = 0
    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books+=1

    @classmethod
    def from_string(cls,book_str):
        title,author = book_str.split("-")
        return Book(title,author)

b1 = Book("Geethanjali","Rabindranath Tagore")
print(f'Title : {b1.title}')
print(f'Author : {b1.author}')
print()
b2 = Book.from_string("Wings of Fire-A P J Abdhul Kalam")
print(b2.title)
print(b2.author)
print()
print(Book.total_books)