from django.shortcuts import render, redirect

from .models import Book

from django.db.models import Q

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse


def logout_view(request):

    logout(request)

    return redirect('login')


def book_list(request):

    query = request.GET.get('q')

    category = request.GET.get('category')

    books = Book.objects.all()

    if query:

        books = books.filter(

            Q(title__icontains=query) |

            Q(author__icontains=query)

        )

    if category:

        books = books.filter(

            category__icontains=category

        )

    return render(request, 'book_list.html', {

        'books': books

    })


def add_book(request):

    if request.user.role not in ['admin', 'librarian']:

        return HttpResponse("Access Denied")

    if request.method == 'POST':

        title = request.POST['title']

        author = request.POST['author']

        isbn = request.POST['isbn']

        quantity = request.POST['quantity']

        category = request.POST['category']

        Book.objects.create(

            title=title,

            author=author,

            isbn=isbn,

            quantity=quantity,

            category=category

        )

        return redirect('book_list')

    return render(request, 'add_book.html')


def restock_book(request, id):

    book = Book.objects.get(id=id)

    book.quantity += 5

    book.save()

    return redirect('book_list')


def edit_book(request, id):

    if request.user.role not in ['admin', 'librarian']:

        return HttpResponse("Access Denied")

    book = Book.objects.get(id=id)

    if request.method == 'POST':

        book.title = request.POST['title']

        book.author = request.POST['author']

        book.isbn = request.POST['isbn']

        book.quantity = request.POST['quantity']

        book.category = request.POST['category']

        book.save()

        return redirect('book_list')

    return render(request, 'edit_book.html', {

        'book': book

    })


def delete_book(request, id):

    if request.user.role not in ['admin', 'librarian']:

        return HttpResponse("Access Denied")

    book = Book.objects.get(id=id)

    book.delete()

    return redirect('book_list')