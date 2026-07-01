from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('librarian-dashboard/', views.librarian_dashboard, name='librarian_dashboard'),

    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    path('logout/', views.logout_view, name='logout'),

    path('register/', views.register_view, name='register'),

    path( 'add-librarian/',views.add_librarian,name='add_librarian'),

    path( 'manage-librarians/', views.manage_librarians,name='manage_librarians'),

    path('edit-librarian/<int:id>/',views.edit_librarian, name='edit_librarian'),


    path( 'delete-librarian/<int:id>/',views.delete_librarian,name='delete_librarian'),

    path('manage-students/',views.manage_students,name='manage_students'),


    path( 'edit-student/<int:id>/',views.edit_student,name='edit_student'),

    path('delete-student/<int:id>/',views.delete_student, name='delete_student'),

    path( 'pending-students/',views.pending_students,name='pending_students'),

    path('approve-student/<int:id>/',views.approve_student,name='approve_student'),







]