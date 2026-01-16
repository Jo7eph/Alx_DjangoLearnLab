from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display title, author, and publication_year in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for publication_year and author
    list_filter = ('publication_year', 'author')
    
    # Enable search capabilities for title and author
    search_fields = ('title', 'author')

# Register the model with the custom configuration
admin.site.register(Book, BookAdmin)