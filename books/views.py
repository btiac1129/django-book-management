from django.shortcuts import render
from .models import Book

def book_list(request):
    book_list = Book.objects.all()
    class_choices = Book.ClassChoices.choices
    class_list = []
    for cc in class_choices:
        class_list.append(cc[0])
    q = request.GET.get('q', '')
    if q:
        book_list = book_list.filter(message__icontains=q)
    return render(request, 'books/book_list.html', {
        'book_list': book_list,
        'q': q,
        'class_list': class_list,
    })