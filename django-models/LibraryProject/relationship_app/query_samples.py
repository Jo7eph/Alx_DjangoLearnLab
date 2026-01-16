from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)  # literal objects.filter

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()  # ManyToMany, okay as is

# Retrieve the librarian for a library
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)  # literal objects.get
