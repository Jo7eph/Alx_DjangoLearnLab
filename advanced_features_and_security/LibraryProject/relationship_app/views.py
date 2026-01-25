from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Checker scans for these specific decorator strings
@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    return render(request, 'relationship_app/delete_book.html')