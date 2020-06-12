from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        'all_books' : Book.objects.all(),
    }
    return render(request, 'index.html', context)

def process_books(request):
    Book.objects.create(
        title = request.POST['title'],
        description = request.POST['description'],
    )
    return redirect('/')

def process_authors(request):
    this_book = Book.objects.get(id=request.POST['book'])
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        book = this_book
    )
    return redirect('/')

def get_books(request):
    context = {
        'book_by_id' : Book.objects.get(id=request.POST['book'])
    }
    return render(request, 'book_info.html', context)

def get_authors(request):
    context = {
        'author_by_id' : Author.objects.get(id=request.POST['author'])
    }
    return render(request, 'author_info.html', context)