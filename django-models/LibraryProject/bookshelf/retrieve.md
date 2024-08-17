from bookshelf.models import Book:

book = Book.objects.get (title="1994")
print (book.tittle, book.author, book.publication_year)

Expected output: 1984 George Orwell 1949