from django.test import TestCase, Client
from django.urls import reverse

from .models import Category


class HomeViewTest(TestCase):
    """Tests for Home View."""

    def setUp(self):
        self.client = Client()

        Category.objects.create(name='category1')
        Category.objects.create(name='category2')
        Category.objects.create(name='category3')

    def test_home_page_route_is_successful(self):
        response = self.client.get(reverse('books:home'))

        self.assertEqual(response.status_code, 200)

    def test_categories_are_on_home_page(self):
        response = self.client.get(reverse('books:home'))

        self.assertQuerysetEqual(response.context['categories'],
            ['<Category: category1>', '<Category: category2>', '<Category: category3>'],
            ordered=False
        )
        self.assertContains(response, 'category1')
