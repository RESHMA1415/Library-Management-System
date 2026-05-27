from django.shortcuts import render, redirect
from accounts.models import CustomUser
from books.models import Book
from .models import IssueBook, BookRequest
from django.http import HttpResponse

from reportlab.pdfgen import canvas




def return_book(request, id):

    issued_book = IssueBook.objects.get(id=id)

    today = timezone.now().date()

    if today > issued_book.due_date:

        late_days = (today - issued_book.due_date).days

        issued_book.fine = late_days * 5

        issued_book.save()

    return render(request, 'fine.html', {

        'issued_book': issued_book

    })


def request_return(request, id):

    issued_book = IssueBook.objects.get(id=id)

    issued_book.return_request = True

    issued_book.save()

    return redirect('my_books')


def return_requests(request):

    books = IssueBook.objects.filter(

        return_request=True

    )

    return render(request, 'return_requests.html', {

        'books': books

    })


def issue_book(request):

    students = CustomUser.objects.filter(role='student')

    books = Book.objects.all()

    if request.method == 'POST':

        student_id = request.POST['student']

        book_id = request.POST['book']

        student = CustomUser.objects.get(id=student_id)

        book = Book.objects.get(id=book_id)

        IssueBook.objects.create(

            student=student,
            book=book

        )

        return redirect('issued_books')

    return render(request, 'issue_book.html', {

        'students': students,
        'books': books

    })


def issued_books(request):

    issued = IssueBook.objects.all()

    return render(request, 'issued_books.html', {

        'issued': issued

    })

def my_books(request):

    books = IssueBook.objects.filter(

        student=request.user

    )

    return render(request, 'my_books.html', {

        'books': books

    })


def request_book(request, id):

    book = Book.objects.get(id=id)

    BookRequest.objects.create(

        student=request.user,
        book=book

    )

    return redirect('my_books')


def my_requests(request):

    requests = BookRequest.objects.filter(

        student=request.user

    )

    return render(request, 'my_requests.html', {

        'requests': requests

    })


def book_requests(request):

    requests = BookRequest.objects.all()

    return render(request, 'book_requests.html', {

        'requests': requests

    })


def approve_request(request, id):

    req = BookRequest.objects.get(id=id)

    if req.book.quantity > 0:

        IssueBook.objects.create(

            student=req.student,
            book=req.book

        )

        req.book.quantity -= 1

        req.book.save()

        req.status = 'Approved'

        req.save()

    else:

        req.status = 'Out of Stock'

        req.save()

    return redirect('book_requests')



def download_report(request):

    response = HttpResponse(

        content_type='application/pdf'

    )

    response['Content-Disposition'] = (

        'attachment; filename="issued_books.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.setFont("Helvetica-Bold", 18)

    pdf.drawString(

        180,
        800,
        "Issued Books Report"

    )
    
    issued_books = IssueBook.objects.all()

    y = 750

    pdf.setFont("Helvetica", 12)

    for item in issued_books:

        text = (

            f"{item.student.username} - "

            f"{item.book.title} - "

            f"Fine: ₹{item.fine}"

        )

        pdf.drawString(50, y, text)

        y -= 30

    pdf.save()

    return response