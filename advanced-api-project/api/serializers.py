from rest_framework import serializers
from .models import Author, Book
import datetime

"""
BookSerializer:
Serializes all fields of the Book model.
Includes custom validation to ensure publication_year
is not in the future.
"""
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


"""
AuthorSerializer:
Serializes the Author model.
Includes a nested BookSerializer to dynamically
serialize all related books for each author.
"""
class AuthorSerializer(serializers.ModelSerializer):

    # Nested serializer for one-to-many relationship
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
