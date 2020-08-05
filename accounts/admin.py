from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'reserved_books_count', 'books_on_load',
                    'is_active', 'is_staff', 'is_superuser']

    def reserved_books_count(self, User):
        return f"{len(User.reserved_books.get_queryset())}권"

    def books_on_load(self, User):
        qs = User.onloaded_books.get_queryset()
        onloaded_list = []
        for q in qs:
            onloaded_list.append(q.title)
        return onloaded_list


