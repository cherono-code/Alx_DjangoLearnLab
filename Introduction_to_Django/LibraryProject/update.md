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
```

## Expected Output
```
Updated book: Nineteen Eighty-Four by George Orwell (1949)
New title: Nineteen Eighty-Four
```

## Explanation
To update a record, you retrieve the object, modify its attributes, and then call the `save()` method to persist the changes to the database. The `save()` method updates the existing record rather than creating a new one.

