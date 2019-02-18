from django.db import models
import datetime


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=300)
    school_email_id = models.EmailField(max_length=254,null=True, blank=True)
    principal_name = models.CharField(max_length=300,null=True, blank=True)
    phone_number = models.CharField(max_length=10,null=True, blank=True)
    school_address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.school_name


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=256)
    date_of_publication = models.DateField(null=True, default=datetime.date.today)
    no_of_pages = models.BigIntegerField()

    def __str__(self):
        return self.book_title


class Student(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    student_email_id = models.EmailField(max_length=254, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6, null=True, blank=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    total_no_of_pages_read = models.BigIntegerField(default=0)

    def __str__(self):
        return self.first_name+ ' ' + self.last_name


class StudentBookRel(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_of_issue = models.DateField()








