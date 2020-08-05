from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('loan/<int:pk>', views.loan_book, name='loan'),
    path('reserve/<int:pk>', views.reserve_book, name='reserve'),
    path('return/<int:pk>', views.return_book, name='return'),
    path('cancel/<int:pk>', views.cancel_book, name='cancel'),
]
