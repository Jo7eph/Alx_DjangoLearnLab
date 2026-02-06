from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
BookListView:
- GET: Retrieve all books
- Access: Public (read-only)
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
BookDetailView:
- GET: Retrieve a single book by ID
- Access: Public (read-only)
"""
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


"""
BookCreateView:
- POST: Create a new book
- Access: Authenticated users only
"""
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
BookUpdateView:
- PUT / PATCH: Update an existing book
- Access: Authenticated users only
"""
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


"""
BookDeleteView:
- DELETE: Remove a book
- Access: Authenticated users only
"""
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
