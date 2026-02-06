from django.db import models

class Author(models.Model):
    """
    Author model to store the name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model linked to an Author with a foreign key.
    One author can have multiple books.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # Relationship: ForeignKey links Book to Author
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title