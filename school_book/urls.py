from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Student
    path('students', views.StudentList.as_view(), name='student_list'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='student_detail'),
    path('students/create', views.StudentCreate.as_view(), name='student_create'),
    path('students/update/<int:pk>', views.StudentUpdate.as_view(), name='student_edit'),
    path('students/delete/<int:pk>', views.StudentDelete.as_view(), name='student_delete'),
    path('students/search', views.search_students, name='student_search'),
    # school
    path('schools', views.SchoolList.as_view(), name='school_list'),
    path('schools/<int:pk>', views.SchoolDetail.as_view(), name='school_detail'),
    path('schools/create', views.SchoolCreate.as_view(), name='school_create'),
    path('schools/update/<int:pk>', views.SchoolUpdate.as_view(), name='school_edit'),
    path('schools/delete/<int:pk>', views.SchoolDelete.as_view(), name='school_delete'),
    path('schools/search', views.search_school, name='school_search'),
    #book
    path('books', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>', views.BookDetail.as_view(), name='book_detail'),
    path('books/create', views.BookCreate.as_view(), name='book_create'),
    path('books/update/<int:pk>', views.BookUpdate.as_view(), name='book_edit'),
    path('books/delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
    path('books/search', views.search_book, name='book_search'),
    #request
    path('books/request', views.request_book, name='book_request'),
    path('data/import', views.data_import, name='data_import'),
]