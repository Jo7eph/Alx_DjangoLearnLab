from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model and validates the publication year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    # Check: Validation to ensure year is not in the future
    def validate(self, data):
        if data['publication_year'] > datetime.date.today().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return data

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author and nests the BookSerializer for a complete representation.
    """
    # Check: This nested field is mandatory
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']