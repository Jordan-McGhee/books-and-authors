from django.shortcuts import render, HttpResponse, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'all_books' : Book.objects.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, 'index.html', context)

def books(request):
    context = {
        'all_books' : Book.objects.all()
    }
    return render(request, 'books.html', context)

def show_book(request, id):
    context = {
        'all_books' : Book.objects.all(),
        'this_book' : Book.objects.get(id=id),
        'all_authors': Author.objects.all()
        }
    return render(request, 'specific_book.html', context)

def create_book(request):
    if request.method == "POST":
        Book.objects.create(title=request.POST['title'], description=request.POST['description'])
        return redirect('/books')

    return redirect('/books')

def add_author(request, id):
    if request.method=="POST":
        this_book = Book.objects.get(id=id)
        author = Author.objects.get(id=request.POST['author'])

        this_book.authors.add(author)

    return redirect(f'/books/{id}')


def authors(request):
    context = {
        'all_authors' : Author.objects.all()
    }
    return render(request, 'authors.html', context)

def show_author(request, id):
    context = {
        'all_books' : Book.objects.all(),
        'this_author' : Author.objects.get(id=id),
        'all_authors': Author.objects.all()
        }
    return render(request, 'specific_author.html', context)

def create_author(request):
    if request.method == "POST":
        Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
        return redirect('/authors')

    return redirect('/authors')

def add_book(request, id):
    if request.method=="POST":
        this_author = Author.objects.get(id=id)
        book = Book.objects.get(id=request.POST['book'])

        this_author.books.add(book)

    return redirect(f'/authors/{id}')