# Create Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output
```
Created book: 1984 by George Orwell (1949)
Book ID: 1
Title: 1984
Author: George Orwell
Publication Year: 1949
```

## Explanation
The `create()` method creates a new Book instance and saves it to the database in a single step. It returns the created object with its primary key (id) automatically assigned by Django.

