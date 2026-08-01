from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Book

def book_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query) | books.filter(author__icontains=query)

    if category:
        books = books.filter(category=category)

    return render(request, 'catalog/book_list.html', {'books': books})


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'catalog/book_detail.html', {'book': book})

# Create your views here.
