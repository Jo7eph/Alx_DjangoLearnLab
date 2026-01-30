from django.urls import path
from .views import BookList

urlpatterns = [
    # This maps the URL to the view using path()
    path('books/', BookList.as_view(), name='book-list'),
]