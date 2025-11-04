from django.shortcuts import get_object_or_404,render
from django.http import Http404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):

  """
  Displays a list of all books and shows their average rating.
  """

  books = Book.objects.all().order_by("title")
  num_books = books.count()

  # Calculate the average rating of all books
  # Returning a dictionary like {'rating__avg': 4.2}
  avg_rating = books.aggregate(Avg("rating"))
  context = {
    "books": books,
    "total_number_of_books":num_books,
    "average_rating":avg_rating
    }
  return render(request,"book_outlet/index.html",context)


def book_detail(request,slug):
  """
    Displays details for a single book, identified by its slug.
  """
  
  # Retrieves the Book object by slug, raising Http404 if it doesn't exist
  book = get_object_or_404(Book,slug=slug)
  context = {
    "title":book.title,
    "author":book.author,
    "rating":book.rating,
    "is_bestseller":book.is_bestselling
  }
  return render(request,"book_outlet/book_detail.html",context)


