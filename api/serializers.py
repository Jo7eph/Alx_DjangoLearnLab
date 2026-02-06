from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes all fields of the Book model and includes 
    custom validation for the publication year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    # Check: Validation to ensure year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes the Author name and dynamically includes 
    all related books using a nested BookSerializer.
    """
    # Check: Nested serializer to handle one-to-many relationship
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']