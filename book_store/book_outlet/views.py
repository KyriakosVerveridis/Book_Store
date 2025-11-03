from django.shortcuts import render
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
