## Filtering, Searching, and Ordering

### Filtering
Books can be filtered by:
- title
- publication_year
- author

Example:
GET /api/books/?publication_year=2020

### Searching
Text search is enabled on:
- title
- author name

Example:
GET /api/books/?search=Orwell

### Ordering
Books can be ordered by:
- title
- publication_year

Example:
GET /api/books/?ordering=-publication_year
