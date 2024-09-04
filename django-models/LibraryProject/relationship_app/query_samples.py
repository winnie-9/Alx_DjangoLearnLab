from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Author Name"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# List all books in a library
library_name = "Library Name"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {librarian.name}")