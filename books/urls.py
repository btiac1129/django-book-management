from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('<int:pk>/loan/', views.loan_book, name='loan'),
    path('<int:pk>/reserve', views.reserve_book, name='reserve'),
    path('<int:pk>/return/', views.return_book, name='return'),
    path('<int:pk>/cancel/', views.cancel_book, name='cancel'),
    path('<int:pk>/detail/', views.book_detail, name='detail'),
]
