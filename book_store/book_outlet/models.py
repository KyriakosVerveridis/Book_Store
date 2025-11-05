from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    """
    Model representing a Book.

    Changes made in this version:
    - Added 'author' field (optional, max length 100)
    - Added 'is_bestselling' boolean field (default=False)
    - Added validators for 'rating' to ensure values between 1 and 5.
    """

    title = models.CharField(max_length=50)  # Title of the book
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )  # Rating between 1 και 5
    author = models.CharField(null=True, max_length=100)  # Author's name, optional
    is_bestselling = models.BooleanField(default=False)  # True if the book is a bestseller

    # Stores a URL-friendly version of the title.
    # Automatically generated in the admin via prepopulated_fields.
    slug = models.SlugField(
        default="",
        null=False,
        blank=True,
        db_index=True,
        primary_key=True,
    )

    def get_absolute_url(self):
        """
        Returns the canonical URL for this Book instance using Django's reverse() function.
        Enables dynamic URL generation instead of hardcoding paths in templates or views.
        """
        return reverse("book-detail", args=[self.slug])

    # The slug field is now automatically generated in the Django admin
    # using the prepopulated_fields option, so the custom save() method
    # is no longer required.

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self):
        """String representation of the Book object."""
        return f"{self.title} ({self.rating})"
