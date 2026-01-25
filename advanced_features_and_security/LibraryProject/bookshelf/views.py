# bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm
from .models import Book

def book_search(request):
    query = request.GET.get('q')
    if query:
        # SECURE: Using ORM parameterization to prevent SQL Injection
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Form validation handles sanitization of input
            form.save()
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})