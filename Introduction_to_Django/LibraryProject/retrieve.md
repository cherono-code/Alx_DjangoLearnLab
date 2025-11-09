# Retrieve Operation

## Command
```python
from bookshelf.models import Book

retrieved_book = Book.objects.get(id=1)
print(f"Retrieved book: {retrieved_book}")
print(f"All attributes:")
print(f"  ID: {retrieved_book.id}")
print(f"  Title: {retrieved_book.title}")
print(f"  Author: {retrieved_book.author}")
print(f"  Publication Year: {retrieved_book.publication_year}")
# Expected output: Retrieved book: 1984 by George Orwell (1949)
# All attributes:
#   ID: 1
#   Title: 1984
#   Author: George Orwell
#   Publication Year: 1949
```

