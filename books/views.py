from django.shortcuts import render
from django.views import View

from .models import Category


class HomeView(View):
    def get(self, request):
        categories = Category.objects.all()

        context = {
            'categories': categories
        }
        return render(request, 'books/home.html', context)
