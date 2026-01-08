from django.db import models

# Model name must be "Book"
class Book(models.Model):
    # Field names must be title, author, and publication_year
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title