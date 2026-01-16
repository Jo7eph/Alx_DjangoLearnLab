from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Library

# Function-based view: List all books
def list_books(request):
    books = Book.objects.all()
    # Point to the correct template path
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Show library details with all books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

