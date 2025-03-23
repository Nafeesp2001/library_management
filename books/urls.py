from django.urls import path
from .views import AdminSignupView, AdminLoginView, BookListCreateView, BookRetrieveUpdateDestroyView, StudentBookListView,student_books_page
from .views import StudentBookListView
urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', AdminLoginView.as_view(), name='admin-login'),
    path('books/', BookListCreateView.as_view(), name='books-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('student/books/', StudentBookListView.as_view(), name='student-books-list'),
    path('student/', student_books_page, name='student-books-page'),
]
