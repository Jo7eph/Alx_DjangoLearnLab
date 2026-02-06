from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework  

# IMPORT YOUR MODELS AND SERIALIZERS
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


"""
BookListView:
- GET: Retrieve all books
- Features:
  - Filtering by title, author, publication_year
  - Search by title and author name
  - Ordering by title and publication_year
- Access: Read-only for unauthenticated users
"""
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        rest_framework.DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    ]
    filterset_fields = ['title', 'publication_year', 'author']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']




"""
BookDetailView:
- GET: Retrieve a single book by ID
- Access: Read-only for unauthenticated users
"""
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


"""
BookCreateView:
- POST: Create a new book
- Access: Authenticated users only
"""
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


"""
BookUpdateView:
- PUT / PATCH: Update a book
- Access: Authenticated users only
"""
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


"""
BookDeleteView:
- DELETE: Delete a book
- Access: Authenticated users only
"""
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
