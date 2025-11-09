# CRUD Operations Documentation

This document contains all CRUD (Create, Read, Update, Delete) operations performed on the Book model in the Django shell.

## Setup

First, import the Book model:
```python
from bookshelf.models import Book
```

---

## 1. CREATE Operation

### Command
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

### Output
```
Created book: 1984 by George Orwell (1949)
Book ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
```

### Notes
- The `create()` method creates and saves a new Book instance in a single step
- Django automatically assigns a primary key (id) to the new record

---

## 2. RETRIEVE Operation

### Command
```python
retrieved_book = Book.objects.get(id=1)
print(f"Retrieved book: {retrieved_book}")
print(f"All attributes:")
print(f"  ID: {retrieved_book.id}")
print(f"  Title: {retrieved_book.title}")
print(f"  Author: {retrieved_book.author}")
print(f"  Publication Year: {retrieved_book.publication_year}")
```

### Output
```
Retrieved book: 1984 by George Orwell (1949)
All attributes:
  ID: 1
  Title: 1984
  Author: George Orwell
  Publication Year: 1949
```

### Notes
- The `get()` method retrieves a single object matching the criteria
- Raises `DoesNotExist` if no object is found
- Raises `MultipleObjectsReturned` if more than one object matches

---

## 3. UPDATE Operation

### Command
```python
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=1)
print(f"Updated book: {updated_book}")
print(f"New title: {updated_book.title}")
```

### Output
```
Updated book: Nineteen Eighty-Four by George Orwell (1949)
New title: Nineteen Eighty-Four
```

### Notes
- Modify the object's attributes
- Call `save()` to persist changes to the database
- The `save()` method updates the existing record

---

## 4. DELETE Operation

### Command
```python
book = Book.objects.get(id=1)
book_id = book.id
book.delete()
print(f"Deleted book with ID: {book_id}")
print("Attempting to retrieve all books:")
all_books = Book.objects.all()
print(f"Number of books in database: {all_books.count()}")
print(f"All books: {list(all_books)}")
```

### Output
```
Deleted book with ID: 1
Attempting to retrieve all books:
Number of books in database: 0
All books: []
```

### Notes
- The `delete()` method removes the object from the database
- After deletion, the object no longer exists in the database
- Retrieving all books confirms the deletion was successful

---

## Summary

All four CRUD operations were successfully performed:
- ✅ **Create**: Created a new Book instance with title "1984", author "George Orwell", and publication year 1949
- ✅ **Retrieve**: Retrieved and displayed all attributes of the created book
- ✅ **Update**: Updated the title from "1984" to "Nineteen Eighty-Four"
- ✅ **Delete**: Deleted the book and confirmed deletion by checking the database

