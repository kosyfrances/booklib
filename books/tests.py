from django.test import TestCase, Client
from django.urls import reverse

from .models import Category, Book


class HomeViewTest(TestCase):
    """Tests for Home View."""

    def setUp(self):
        self.client = Client()

        self.category1 = Category.objects.create(name='category1')
        self.category2 = Category.objects.create(name='category2')
        self.category3 = Category.objects.create(name='category3')

        Book.objects.create(title='book1', author='author1',
                            category=self.category1)
        Book.objects.create(title='book2', author='author2',
                            category=self.category2)
        Book.objects.create(title='book3', author='author3',
                            category=self.category3)
        Book.objects.create(title='book4', author='author4',
                            category=self.category3)

    def test_home_page_route_is_successful(self):
        response = self.client.get(reverse('books:home'))

        self.assertEqual(response.status_code, 200)

    def test_categories_are_on_home_page(self):
        response = self.client.get(reverse('books:home'))

        self.assertQuerysetEqual(response.context['categories'],
            ['<Category: category1>', '<Category: category2>',
             '<Category: category3>'], ordered=False
        )
        self.assertContains(response, 'category1')

    def test_books_are_on_home_page(self):
        response = self.client.get(reverse('books:home'))

        self.assertQuerysetEqual(response.context['books'],
            ['<Book: book1>', '<Book: book2>', '<Book: book3>',
             '<Book: book4>'], ordered=False
        )
        self.assertContains(response, 'book1')

    def test_user_can_search_books_by_name(self):
        # Search by full book name
        data = {'qname': 'book1'}
        response = self.client.get(reverse('books:home'), data)

        self.assertQuerysetEqual(response.context['books'],
                                 ['<Book: book1>'], ordered=False)

        # Search by keyword from bookname
        data = {'qname': 'ok1'}
        response = self.client.get(reverse('books:home'), data)

        self.assertQuerysetEqual(response.context['books'],
                                 ['<Book: book1>'], ordered=False)

        # Search with non-existent bookname
        data = {'qname': 'blablabla'}
        response = self.client.get(reverse('books:home'), data)

        self.assertQuerysetEqual(response.context['books'], [],
                                 ordered=False)

    def test_user_can_search_by_category(self):
        # Search by full category name
        data = {'qcategory': 'category2'}
        response = self.client.get(reverse('books:home'), data)

        self.assertQuerysetEqual(response.context['books'],
                                 ['<Book: book2>'], ordered=False)

        # Search by keyword from category
        data = {'qcategory': 'categ'}
        response = self.client.get(reverse('books:home'), data)

        self.assertQuerysetEqual(response.context['books'], [],
                                 ordered=False)

        # Search by non-existent category
        data = {'qcategory': 'blablabla'}
        response = self.client.get(reverse('books:home'), data)

        self.assertQuerysetEqual(response.context['books'], [],
                                 ordered=False)
