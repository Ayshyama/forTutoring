from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from app_bookstore.models import Book


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="The Hobbit",
            author="J.R.R. Tolkien",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        Book.objects.create(
            title="The Hobbit",
            author="J.R.R. Tolkien",
        )
        print('First test: ' , Book.objects.all())
        self.assertContains(response, "The Hobbit")