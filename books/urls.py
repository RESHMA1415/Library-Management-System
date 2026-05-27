from django.urls import path
from . import views

urlpatterns = [

    path('books/', views.book_list, name='book_list'),

    path('add-book/', views.add_book, name='add_book'),
    path('restock-book/<int:id>/', views.restock_book, name='restock_book'),
    path('edit-book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),



    

]