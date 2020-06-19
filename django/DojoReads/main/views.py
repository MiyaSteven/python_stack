from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt

def index(request):
    return render(request, "register.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
    hashed = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    if len(errors) > 0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    this_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed,
        confirm_password=hashed
    )
    request.session['user_id'] = this_user.id
    return redirect('/books')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        log_in_user = users[0]
        if  bcrypt.checkpw(request.POST['password'].encode(), log_in_user.password.encode()):
            request.session['user_id'] = log_in_user.id
            return redirect('/books')
    messages.error(request, "Email and/or Password not found")
    return redirect('/')

def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "user": User.objects.get(id=request.session['user_id']),
        "all_users": User.objects.all()
    }
    return render(request, "books.html", context)

def add(request):
    return render(request, "add.html")

# def user_info(request, user_id):
#     user = User.objects.get(id=user_id)
#     context = {
#         "user": user
#     }
#     return render(request, "user_info.html", context)

# def render_books(request):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     return render(request, "add_book_and_review.html")

# def add_book_and_review(request, book_id):
#     book = Book.objects.get(id=book_id)
#     this_book = Book.objects.create(
#         book_title=request.POST['book_title'],
#         author=request.POST['author'],
#         review=request.POST['review'],
#         rating=request.POST['rating']
#     )
#     request.session['book_id'] = this_book.id
#     return redirect('/{{book}}/{{book.id}}') # check to see if this is accessing the book and book.id might be this_book.id

# def book_reviews(request):
#     if 'book_id' not in request.session:
#         return redirect('/add_book_and_review')
#     context = {
#         "book": Book.objects.get(id=request.session['book']),
#         "all_books": Book.objects.all()
#     }
#     return render(request, "book_reviews.html", context)

def logout(request):
    request.session.clear()
    return redirect('/')
