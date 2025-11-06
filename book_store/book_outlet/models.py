from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        """String representation of the Address object."""
        return f"{self.street},{self.postal_code},{self.city}"
    
    class Meta:
        """"Defines the plural name of the model
          as it will appear in the Django admin"""
        verbose_name_plural = "Address Entries"


class Author(models.Model):
    """
    Represents an author with first and last name.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) # Creates a one-to-one relationship with Address

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        """String representation of the Author object."""
        return self.full_name()


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
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,
                               related_name="books") # Link to an Author record.
    is_bestselling = models.BooleanField(default=False)  # True if the book is a bestseller.
    slug = models.SlugField(default="", null=False, blank=True, db_index=True) # Stores a URL-friendly version of the title.
                                                                               # Automatically generated in the admin via prepopulated_fields. 
    published_countries = models.ManyToManyField(Country) # Links the object to multiple countries

    def get_absolute_url(self):
        """
        Returns the canonical URL for this Book instance using Django's reverse() function.
        Enables dynamic URL generation instead of hardcoding paths in templates or views.
        """
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        """String representation of the Book object."""
        return f"{self.title} ({self.rating})"
