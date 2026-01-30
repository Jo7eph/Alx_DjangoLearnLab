from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer

# Existing ListAPIView from previous task
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD functionality
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer