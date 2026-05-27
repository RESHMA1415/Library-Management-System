from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponse

from .models import CustomUser

from books.models import Book

from books.models import IssuedBook


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        user = authenticate(

            request,

            username=username,

            password=password

        )

        if user is not None:

            if user.role == 'librarian':

                if user.is_blocked == True:

                    return HttpResponse(

                        "Your Account is Blocked"

                    )

            login(request, user)

            if user.role == 'admin':

                return redirect('admin_dashboard')

            elif user.role == 'librarian':

                return redirect('librarian_dashboard')

            elif user.role == 'student':

                return redirect('student_dashboard')

    return render(request, 'login.html')


def register_view(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        CustomUser.objects.create_user(

            username=username,

            email=email,

            password=password,

            role='student'

        )

        return redirect('login')

    return render(request, 'register.html')


def admin_dashboard(request):

    return render(request, 'admin_dashboard.html')


def librarian_dashboard(request):

    return render(request, 'librarian_dashboard.html')


def student_dashboard(request):

    return render(request, 'student_dashboard.html')


def logout_view(request):

    logout(request)

    return redirect('login')



# def admin_dashboard(request):

#     total_books = Book.objects.count()

#     total_students = CustomUser.objects.filter(

#         role='student'

#     ).count()

#     total_librarians = CustomUser.objects.filter(

#         role='librarian'

#     ).count()

#     issued_books = IssuedBook.objects.count()

#     return render(

#         request,

#         'admin_dashboard.html',

#         {

#             'total_books': total_books,

#             'total_students': total_students,

#             'total_librarians': total_librarians,

#             'issued_books': issued_books

#         }

#     )


def add_librarian(request):

    if request.method == 'POST':

        username = request.POST['username']

        email = request.POST['email']

        password = request.POST['password']

        CustomUser.objects.create_user(

            username=username,

            email=email,

            password=password,

            role='librarian',

            is_approved=True

        )

        return redirect('admin_dashboard')

    return render(

        request,

        'add_librarian.html'

    )




def manage_librarians(request):

    librarians = CustomUser.objects.filter(

        role='librarian'

    )

    return render(

        request,

        'manage_librarians.html',

        {

            'librarians': librarians

        }

    )


def edit_librarian(request, id):

    librarian = CustomUser.objects.get(id=id)

    if request.method == 'POST':

        librarian.username = request.POST['username']

        librarian.email = request.POST['email']

        librarian.save()

        return redirect('manage_librarians')

    return render(

        request,

        'edit_librarian.html',

        {

            'librarian': librarian

        }

    )

def delete_librarian(request, id):

    librarian = CustomUser.objects.get(id=id)

    librarian.delete()

    return redirect('manage_librarians')


def manage_students(request):

    students = CustomUser.objects.filter(

        role='student'

    )

    return render(

        request,

        'manage_students.html',

        {

            'students': students

        }

    )


def edit_student(request, id):

    student = CustomUser.objects.get(id=id)

    if request.method == 'POST':

        student.username = request.POST['username']

        student.email = request.POST['email']

        student.save()

        return redirect('manage_students')

    return render(

        request,

        'edit_student.html',

        {

            'student': student

        }

    )

def delete_student(request, id):

    student = CustomUser.objects.get(id=id)

    student.delete()

    return redirect('manage_students')