from django.contrib import admin
from .models import IssueBook
from .models import IssueBook, BookRequest

admin.site.register(IssueBook)
admin.site.register(BookRequest)

# Register your models here.
