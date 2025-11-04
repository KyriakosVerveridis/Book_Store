from django.shortcuts import get_object_or_404,render
from django.http import Http404
from .models import Book

# Create your views here.

def index(request):

  """
    View function for displaying all books in the outlet.
    Retrieves all Book objects from the database and renders them
    in the 'index.html' template.
  """
  books = Book.objects.all()
  context = {"books": books}
  return render(request,"book_outlet/index.html",context)


def book_detail(request,id):
  """
    Fetches a single Book by its primary key (pk) and passes its
    title, author, rating, and bestseller status to the template.
    """
  
  # Fetch the Book with the given primary key (pk) or return 404 if not found
  book = get_object_or_404(Book,pk=id)
  context = {
    "title":book.title,
    "author":book.author,
    "rating":book.rating,
    "is_bestseller":book.is_bestselling
  }
  return render(request,"book_outlet/book_detail.html",context)


