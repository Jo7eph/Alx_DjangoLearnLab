from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = TaggableManager()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
