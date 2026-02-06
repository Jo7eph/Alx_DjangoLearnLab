from django.db import models

class Author(models.Model):
    """
    Author model: Stores the author's name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model: Linked to an Author. 
    One author can have multiple books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # REQUIRED: related_name must be 'books' for the serializer to work
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title