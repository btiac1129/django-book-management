from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Book

def book_list(request):
    book_list = Book.objects.all()
    class_choices = Book.ClassChoices.choices
    class_list = []
    for cc in class_choices:
        class_list.append(cc[0])
    q = request.GET.get('q', '')
    if q:
        book_list = book_list.filter(title__icontains=q)
    return render(request, 'books/book_list.html', {
        'book_list': book_list,
        'q': q,
        'class_list': class_list,
    })

def book_detail(request, pk):
    book_id = pk
    book = Book.objects.get(pk=pk)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })

def book_search(request, title):
    book_title = title
    qs = request.GET
    book = Book.objects.filter(title__contains=book_title)
    return render(request, 'books/book_search_form.html', {
        'book': book,
    })

@login_required
def loan_book(request, pk):
    book_id = pk
    user = request.user
    book = Book.objects.get(pk=book_id)
    user.loan_record.add(book)
    user.onloaded_books.set([book])
    book.isOnload = True
    book.save()
    return redirect('accounts:profile', username=user.username)

@login_required
def reserve_book(request, pk):
    book_id = pk
    user = request.user
    book = Book.objects.get(pk=book_id)
    user.reserved_books.add(book)
    book.reservation_number += 1
    user.save()
    book.save()
    return redirect('accounts:profile', username=user.username)

@login_required
def return_book(request, pk):
    book_id = pk
    user = request.user
    book = Book.objects.get(pk=book_id)
    user.onloaded_books.remove(book)
    book.isOnload = False
    user.save()
    book.save()
    return redirect('accounts:profile', username=user.username)

@login_required
def cancel_book(request, pk):
    book_id = pk
    user = request.user
    book = Book.objects.get(pk=book_id)
    user.reserved_books.remove(book)
    book.reservation_number -= 1
    user.save()
    book.save()
    return redirect('accounts:profile', username=user.username)