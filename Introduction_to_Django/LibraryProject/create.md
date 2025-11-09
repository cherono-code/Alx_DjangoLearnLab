# Create Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected output: Created book: 1984 by George Orwell (1949)
# Book ID: 1
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
```

