**Update the title of the created book**
from bookshelf.models import Book:

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

Expected output: Nineteen Eighty-Four