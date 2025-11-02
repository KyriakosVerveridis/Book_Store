from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

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

  def __str__(self):
    return f"{self.title} ({self.rating})"
  