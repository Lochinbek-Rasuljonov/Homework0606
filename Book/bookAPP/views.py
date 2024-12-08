from django.shortcuts import render
from .models import Category, Book

from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def home(request):
    categories = Category.objects.all()
    books = Book.objects.all()
    return render(request, 'index.html', {'categories': categories, 'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})

def books_by_author(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    books = Book.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'books': books,
        'selected_category': category
    })