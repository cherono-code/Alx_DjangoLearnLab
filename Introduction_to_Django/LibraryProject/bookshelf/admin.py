from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Book model.
    Provides enhanced display, filtering, and search capabilities.
    """
    # Display fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Enable filtering by author and publication year
    list_filter = ('author', 'publication_year')
    
    # Enable search functionality for title and author
    search_fields = ('title', 'author')
    
    # Order books by title by default
    ordering = ('title',)
    
    # Display publication year in the list view
    list_display_links = ('title',)
