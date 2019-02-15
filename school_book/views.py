from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Student, Book, School, StudentBookRel


class StudentList(ListView):
    model = Student
    template_name = "school_book/student_list.html"
    fields = ['first_name', 'last_name']
    success_url = reverse_lazy('student_list')


class StudentDetail(DetailView):
    model = Student
    template_name = "school_book/student_detail.html"
    fields = ['first_name', 'last_name','gender','school_id']
    success_url = reverse_lazy('student_detail')


class StudentCreate(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'gender','school_id']
    success_url = reverse_lazy('student_list')


class StudentUpdate(UpdateView):
    model = Student
    fields = ['id','first_name', 'last_name', 'gender', 'school_id']
    success_url = reverse_lazy('student_list')


class StudentDelete(DeleteView):
    model = Student
    fields = ['id']
    success_url = reverse_lazy('student_list')


### Book views
class BookList(ListView):
    model = Book
    template_name = "school_book/book_list.html"
    fields = ['book_title', 'author_name', 'date_of_publication', 'no_of_pages']
    success_url = reverse_lazy('book_list')


class BookDetail(DetailView):
    model = Book
    template_name = "school_book/book_detail.html"
    fields = ['book_title', 'author_name', 'date_of_publication', 'no_of_pages']
    success_url = reverse_lazy('book_detail')


class BookCreate(CreateView):
    model = Book
    fields = ['book_title', 'author_name', 'date_of_publication', 'no_of_pages']
    success_url = reverse_lazy('book_list')


class BookUpdate(UpdateView):
    model = Book
    fields = ['id', 'book_title', 'author_name', 'date_of_publication', 'no_of_pages']
    success_url = reverse_lazy('book_list')


class BookDelete(DeleteView):
    model = Book
    fields = ['id']
    success_url = reverse_lazy('book_list')


### School views
class SchoolList(ListView):
    model = School
    template_name = "school_book/school_list.html"
    fields = ['school_name']
    success_url = reverse_lazy('school_list')


class SchoolDetail(DetailView):
    model = School
    template_name = "school_book/school_detail.html"
    fields = ['school_name', 'school_email_id', 'principal_name', 'school_address', 'phone_number']
    success_url = reverse_lazy('school_detail')


class SchoolCreate(CreateView):
    model = School
    fields = ['school_name', 'school_email_id', 'principal_name', 'school_address', 'phone_number']
    success_url = reverse_lazy('school_list')


class SchoolUpdate(UpdateView):
    model = School
    fields = ['id', 'school_name', 'school_email_id', 'principal_name', 'school_address', 'phone_number']
    success_url = reverse_lazy('school_list')


class SchoolDelete(DeleteView):
    model = School
    fields = ['id']
    success_url = reverse_lazy('school_list')


# class BookRequestList(ListView):
#     model = StudentBookRel
#     template_name = "school_book/book_request_list.html"
#     fields = ['student_id','book_id','date_of_issue']


def index(request):
    block_list =[{
                    'name':'Students',
                    'create_url':'student_create',
                    'list_url':'student_list',
                    'search_url':'student_search',
                },
                 {
                     'name':'School',
                     'create_url':'school_create',
                     'list_url':'school_list',
                     'search_url': 'school_search',
                 },
                 {
                     'name':'Books',
                     'create_url':'book_create',
                     'list_url':'book_list',
                     'search_url': 'book_search',
                 }]
    return render(request, 'school_book/homepage.html', {'block_list': block_list})


def request_book(request):
    student_list = Student.objects.all()
    book_list = Book.objects.all()
    if request.method == 'POST':
        s_id = Student.objects.get(pk=request.POST.get('student_selection'))
        b_id = Book.objects.get(pk=request.POST.get('book_selection'))
        new_request =  StudentBookRel(student_id=s_id, book_id=b_id, date_of_issue=timezone.now().date())
        new_request.save()
        s_id.total_no_of_pages_read += s_id.total_no_of_pages_read + b_id.no_of_pages
        s_id.save()
    std_bk_req_list = StudentBookRel.objects.all()
    return render(request, 'school_book/request_book.html', {'student_list': student_list, 'book_list':book_list,'std_bk_req_list': std_bk_req_list})


def search_students(request):
    print("request====>", request.method)
    error = ''
    try:
        if request.method == 'GET':
            return render(request,'school_book/student_search.html')
        elif request.method == 'POST':
            if request.POST.get('id') and not request.POST.get('first_name') and not request.POST.get('last_name'):
                student = Student.objects.filter(pk=request.POST.get('id'))
            elif not request.POST.get('id') and request.POST.get('first_name') and not request.POST.get('last_name'):
                student = Student.objects.filter(first_name__icontains=request.POST.get('first_name'))
            elif not request.POST.get('id') and not request.POST.get('first_name') and  request.POST.get('last_name'):
                student = Student.objects.filter(last_name__icontains=request.POST.get('last_name'))
            elif request.POST.get('id') and request.POST.get('first_name') and not request.POST.get('last_name'):
                print("only id is and first_name ")
                student = Student.objects.filter(first_name__icontains=request.POST.get('first_name'),
                                                 id=request.POST.get('id'))
            elif request.POST.get('id') and not request.POST.get('first_name') and request.POST.get('last_name'):
                student = Student.objects.filter(last_name__icontains=request.POST.get('last_name'),
                                                 id=request.POST.get('id'))
            elif not request.POST.get('id') and  request.POST.get('first_name') and request.POST.get('last_name'):
                student = Student.objects.filter(last_name__icontains=request.POST.get('last_name'),
                                                 first_name__icontains=request.POST.get('first_name'))
            elif request.POST.get('id') and request.POST.get('first_name') and request.POST.get('last_name'):
                student = Student.objects.filter(last_name__icontains=request.POST.get('last_name'),
                                                 first_name__icontains=request.POST.get('first_name'),
                                                 id=request.POST.get('id'))
            else:
                error = 'Please select atleast one filter'
                return render(request, 'school_book/student_search.html',{'error': error})
            print("Student======>",student)
            if student:
                print("here============")
                return render(request, 'school_book/student_list.html', {'object_list':student, 'error':error})
            else:
                error = 'No students found matching above parameters'
                return render(request, 'school_book/student_search.html', {'error': error})
        else:
            return HttpResponse("<h3>Search Page under construction</h3>")
    except Exception as e:
        return HttpResponse("<h3>Please Provide appropriate input to search page.</h3>")


def search_school(request):
    error = ''
    try:
        if request.method == 'GET':
            return render(request,'school_book/school_search.html')
        elif request.method == 'POST':
            if request.POST.get('school_name'):
                school = School.objects.filter(school_name__icontains=request.POST.get('school_name'))
            else:
                error = 'Please select atleast one filter'
                return render(request, 'school_book/student_search.html', {'error': error})

            print("school======>", school)
            if school:
                return render(request, 'school_book/school_list.html', {'object_list': school, 'error': error})
            else:
                error = 'No School found matching above name'
                return render(request, 'school_book/school_search.html', {'error': error})
        else:
            return HttpResponse("<h3>Search Page under construction</h3>")
    except Exception as e:
        return HttpResponse("<h3>Please Provide appropriate input to search page.</h3>")


def search_book(request):
    error = ''
    try:
        if request.method == 'GET':
            return render(request,'school_book/book_search.html')
        elif request.method == 'POST':
            if request.POST.get('book_title'):
                book = Book.objects.filter(book_title__icontains=request.POST.get('book_title'))
            else:
                error = 'Please select filter'
                return render(request, 'school_book/book_search.html', {'error': error})

            if book:
                return render(request, 'school_book/book_list.html', {'object_list': book, 'error': error})
            else:
                error = 'No Book found matching above name'
                return render(request, 'school_book/book_search.html', {'error': error})
        else:
            return HttpResponse("<h3>Search Page under construction</h3>")
    except Exception as e:
        return HttpResponse("<h3>Please Provide appropriate input to search page.</h3>")
