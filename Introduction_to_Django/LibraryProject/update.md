# Update Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=1)
print(f"Updated book: {updated_book}")
print(f"New title: {updated_book.title}")
# Output:
# Updated book: Nineteen Eighty-Four by George Orwell (1949)
# New title: Nineteen Eighty-Four
```

