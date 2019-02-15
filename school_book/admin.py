from django.contrib import admin
from .models import Book, School, Student, StudentBookRel

# Register your models here.
admin.site.register(Book)
admin.site.register(School)
admin.site.register(Student)
admin.site.register(StudentBookRel)