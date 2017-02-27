from django.shortcuts import render
from django.views import View

from .models import Category, Book


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()
        books = Book.objects.all()

        context = {
            'categories': categories,
            'books': books
        }
        return render(request, 'books/home.html', context)
