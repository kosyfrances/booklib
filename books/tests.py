from django.test import TestCase, Client
from django.urls import reverse


class HomeViewTest(TestCase):
    """Tests for Home View."""

    def setUp(self):
        self.client = Client()

    def test_home_page_route_is_successful(self):
        response = self.client.get(reverse('books:home'))

        self.assertEqual(response.status_code, 200)
