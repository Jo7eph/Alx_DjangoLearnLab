from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True) # Required
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True) # Required

    objects = CustomUserManager()

    # Resolve E304 Clashes by giving unique related_names
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups', # Unique name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions', # Unique name
        blank=True
    )