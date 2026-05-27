from django.urls import path
from . import views

urlpatterns = [

    path('issue-book/', views.issue_book, name='issue_book'),

    path('issued-books/', views.issued_books, name='issued_books'),
    path('return-book/<int:id>/', views.return_book, name='return_book'),
    path('my-books/', views.my_books, name='my_books'),
    path('request-book/<int:id>/', views.request_book, name='request_book'),
    path('book-requests/', views.book_requests, name='book_requests'),

    path('approve-request/<int:id>/', views.approve_request, name='approve_request'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('request-return/<int:id>/', views.request_return, name='request_return'),
    path('return-requests/', views.return_requests, name='return_requests'),
    path('download-report/', views.download_report, name='download_report'),

]