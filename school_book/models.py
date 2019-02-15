from django.db import models


# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=300)
    school_email_id = models.EmailField(max_length=254)
    principal_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=10)
    school_address = models.TextField()

    def __str__(self):
        return self.school_name


class Book(models.Model):
    book_title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=256)
    date_of_publication = models.DateField(auto_now=False)
    no_of_pages = models.BigIntegerField()

    def __str__(self):
        return self.book_title


class Student(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

    GENDER_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_email_id = models.EmailField(max_length=254)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=6)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    total_no_of_pages_read = models.BigIntegerField(default=0)

    def __str__(self):
        return self.first_name+ ' ' + self.last_name


class StudentBookRel(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_of_issue = models.DateField()






