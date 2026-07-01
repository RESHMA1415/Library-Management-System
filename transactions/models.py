from django.db import models

from django.utils import timezone

from datetime import timedelta

from accounts.models import CustomUser

from books.models import Book


class IssueBook(models.Model):

    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    issue_date = models.DateField(default=timezone.now)

    due_date = models.DateField(default=timezone.now() + timedelta(days=7))

    fine = models.IntegerField(default=0)

    return_request = models.BooleanField(default=False)
    

    def __str__(self):

        return self.student.username


class BookRequest(models.Model):

    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE )

    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    status = models.CharField(max_length=20,default='Pending')

   