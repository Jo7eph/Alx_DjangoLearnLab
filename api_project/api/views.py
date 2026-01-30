from rest_framework import viewsets, generics
from .models import Book
from .serializers import BookSerializer

# This was from Task 1
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This is what Task 2 requires - MAKE SURE THIS IS HERE
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer