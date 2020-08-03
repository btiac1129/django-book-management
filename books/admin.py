from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['class_number',
                    'title',
                    'author',
                    'publisher',
                    'subject_keyword',
                    'issued_date',
                    'isbn',
                    'isOnload',
                    'reservation_number']