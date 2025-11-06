from django.contrib import admin
from .models import Book,Author

# Register your models here.

# Register the Author model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin options for the Book model.
    - Automatically generates the slug from the title field.
    """
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author","rating",)
    list_display = ("title","author",)

# Register the Book model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name",)
