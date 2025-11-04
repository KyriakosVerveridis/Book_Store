from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
  """
    Model representing a Book.

    Changes made in this version:
    - Added 'author' field (optional, max length 100)
    - Added 'is_bestselling' boolean field (default=False)
    - Added validators for 'rating' to ensure values between 1 and 5
  """ 
  
  title = models.CharField(max_length=50) # Title of the book
  rating = models.IntegerField(
    validators=[MinValueValidator(1),MaxValueValidator(5)]
    ) # Rating between 1 and 5
  author = models.CharField(null=True,max_length=100) # Author's name, optional
  is_bestselling = models.BooleanField(default=False) # True if the book is a bestseller

  """
   Stores a URL-friendly version of the title,
   generated automatically in save(), e.g., "Harry Potter 1" → "harry-potter-1"
  """
  slug = models.SlugField(default="", null=False, db_index=True, primary_key=True)

  """
    Returns the canonical URL for this Book instance using Django's reverse() function.
    Enables dynamic URL generation instead of hardcoding paths in templates or views.
    """
  def get_absolute_url(self):
      return reverse("book-detail", args=[self.slug])
  

  def save(self,*args,**kwargs):
     
     # Automatically generates a URL-friendly version of the title, e.g., "My Book" → "my-book"
     self.slug = slugify(self.title)

     # Call the original save() method to save the instance to the database
     super().save(*args, **kwargs)
    
  
  def __str__(self):
    return f"{self.title} ({self.rating})"
  
  
  