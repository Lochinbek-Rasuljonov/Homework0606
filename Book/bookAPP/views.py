from django.shortcuts import render
from .models import Category, Book

def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()  #
    return render(request, 'index.html', {'categories': categories, 'books': books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})
