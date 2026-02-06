from django.db import models

# Author model stores the name of book writers
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Book model stores title and year, linked to an Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    # Foreign Key establishes a one-to-many relationship: One author can have many books
    author = models.ForeignKey(Author, related_name='books', on_year=models.CASCADE)

    def __str__(self):
        return self.title