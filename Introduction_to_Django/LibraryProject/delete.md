# Delete Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()
# Expected output: Book deleted successfully
# Confirming deletion:
all_books = Book.objects.all()
print(f"Number of books in database: {all_books.count()}")
print(f"All books: {list(all_books)}")
# Expected output: Number of books in database: 0
# All books: []
```

