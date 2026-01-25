from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# View protected by can_view
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View protected by can_create
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic for creating a book
    return render(request, 'bookshelf/form.html')

# View protected by can_edit
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for editing
    return render(request, 'bookshelf/form.html', {'book': book})

# View protected by can_delete
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('book_list')