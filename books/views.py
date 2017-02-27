from django.shortcuts import render
from django.views import View

from .models import Category, Book


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()

        book_name_keyword = request.GET.get('qname')

        if book_name_keyword:
            books = Book.objects.filter(title__icontains=book_name_keyword)
        else:
            books = Book.objects.all()

        context = {
            'categories': categories,
            'books': books
        }
        return render(request, 'books/home.html', context)
