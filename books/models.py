from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    isbn = models.CharField(max_length=20)

    quantity = models.IntegerField()
    
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title



from django.contrib.auth import get_user_model

User = get_user_model()


class IssuedBook(models.Model):

    student = models.ForeignKey(User, on_delete=models.CASCADE)

    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    issue_date = models.DateField(auto_now_add=True)

    due_date = models.DateField()

    fine = models.IntegerField(default=0)

    return_request = models.BooleanField(default=False)

    def __str__(self):

        return self.book.title