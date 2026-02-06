# Advanced API Project – Custom Views with DRF

## Overview
This project demonstrates the use of Django REST Framework generic views
to build a RESTful API for managing books.

## Views
- BookListView: Retrieve all books (public)
- BookDetailView: Retrieve a single book by ID (public)
- BookCreateView: Create a new book (authenticated only)
- BookUpdateView: Update an existing book (authenticated only)
- BookDeleteView: Delete a book (authenticated only)

## Permissions
Read-only access is allowed for unauthenticated users.
Create, update, and delete operations require authentication.

## Endpoints
- GET /api/books/
- GET /api/books/<id>/
- POST /api/books/create/
- PUT /api/books/<id>/update/
- DELETE /api/books/<id>/delete/
