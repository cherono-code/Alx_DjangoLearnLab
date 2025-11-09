# Delete Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book_id = book.id
book.delete()
print(f"Deleted book with ID: {book_id}")
print("Attempting to retrieve all books:")
all_books = Book.objects.all()
print(f"Number of books in database: {all_books.count()}")
print(f"All books: {list(all_books)}")
```

## Expected Output
```
Deleted book with ID: 1
Attempting to retrieve all books:
Number of books in database: 0
All books: []
```

## Explanation
The `delete()` method removes the object from the database. After deletion, attempting to retrieve all books confirms that the database is now empty, verifying that the deletion was successful.

