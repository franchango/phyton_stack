from django.shortcuts import redirect, render, HttpResponse
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "all_the_books": Book.objects.all()
    }
    return render(request, "index.html", context)

def new_book(request):
    Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

# def view_book(request, book_id):          #basic level
#     context = {
#         "this_book": Book.objects.get(id = book_id),
#         "all_the_authors": Author.objects.all()
#     }
#     return render(request, "view_book.html", context)

def view_book(request, book_id):            #sensei level
    context = {
        "this_book": Book.objects.get(id = book_id),
        "all_the_authors": Author.objects.exclude(books = book_id)
    }
    return render(request, "view_book.html", context)

def add_author(request):
    author_to_add = Author.objects.get(id = request.POST['author_id'])
    book = Book.objects.get(id = request.POST['book_id'])
    author_to_add.books.add(book)
    book_id = request.POST['book_id']
    return redirect(f'/books/{book_id}')

def authors(request):
    context = {
        "all_the_authors": Author.objects.all()
    }
    return render(request, "authors.html", context)

def new_author(request):
    Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect('/authors')

# def view_author(request, author_id):      #basic level
#     context = {
#         "this_author": Author.objects.get(id = author_id),
#         "all_the_books": Book.objects.all()
#     }
#     return render(request, "view_author.html", context)

def view_author(request, author_id):        #sensei level
    context = {
        "this_author": Author.objects.get(id = author_id),
        "all_the_books": Book.objects.exclude(authors = author_id)
    }
    return render(request, "view_author.html", context)



def add_book(request):
    book_to_add = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = request.POST['author_id'])
    book_to_add.authors.add(author)
    author_id = request.POST['author_id']
    return redirect(f'/authors/{author_id}')