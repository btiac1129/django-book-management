from django.shortcuts import render
from .models import Book

def book_list(request):
    qs = Book.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)
    return render(request, 'books/book_list.html', {
        'book_list': qs,
        'q': q,
    })