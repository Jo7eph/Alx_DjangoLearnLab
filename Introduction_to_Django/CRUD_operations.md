# Django ORM CRUD Operations Log

## 1. Create
- **Command**: `Book.objects.create(title="1984", author="George Orwell", publication_year=1949)`
- **Result**: Book object created with ID 1.

## 2. Retrieve
- **Command**: `Book.objects.get(title="1984")`
- **Result**: Retrieved `<Book: 1984>` with all attributes intact.

## 3. Update
- **Command**: `book.title = "Nineteen Eighty-Four"`, followed by `book.save()`
- **Result**: The title attribute in the database was successfully updated.

## 4. Delete
- **Command**: `book.delete()`
- **Result**: The book was removed. `Book.objects.all()` returned an empty QuerySet.