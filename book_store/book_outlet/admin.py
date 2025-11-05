from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin options for the Book model.
    - Automatically generates the slug from the title field.
    """
    prepopulated_fields = {"slug": ("title",)}
