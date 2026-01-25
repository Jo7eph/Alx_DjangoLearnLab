# Permissions and Groups Setup

## Custom Permissions
The `Book` model includes the following custom permissions:
- `can_view`: Allows users to view the book list.
- `can_create`: Allows users to add new books.
- `can_edit`: Allows users to modify existing book details.
- `can_delete`: Allows users to remove books from the library.

## Groups Configuration
1. **Viewers**: Can only view books.
2. **Editors**: Can view, create, and edit books.
3. **Admins**: Have full permissions including deletion.