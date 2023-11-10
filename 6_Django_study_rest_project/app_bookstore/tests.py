from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book


# Create your tests here.

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='testuser',
            password='123456',
            is_superuser=True
        )

        cls.book = Book.objects.create(
            title='Test Title',
            author='Test Author',
            published_date='2021-01-01',
            price=200,
            stock=20
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, 'Test Title')
        self.assertEqual(str(self.book), self.book.title)

    
    def test_book_retreave(self):
        book_from_db = Book.objects.get(id=self.book.id)
        book_from_db_filter = Book.objects.filter(title='Test Title')

        self.assertEqual(book_from_db, self.book)

    def test_book_update(self):
        self.book.title = 'An updated title'
        self.book.save()
        book_from_db = Book.objects.get(id=self.book.id).title

        self.assertEqual(book_from_db, "An updated title")

    
    def test_book_deletion(self):
        book_id = self.book.id
        self.book.delete()

        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)


    def test_str_representation(self):
        self.assertEqual(str(self.book), 'Test Title')

    def test_get_absolute_urls(self):
        expected_url = f'/books/{self.book.id}/'
        self.assertEqual(self.book.get_absolute_url(), expected_url)

    

class UrlTest(TestCase):

    def test_get_absolute_urls_response(self):
        url = reverse('book_list')
        print(url)
        response = self.client.get(reverse("book_list"))
        print(response.request)
        self.assertEqual(response.status_code, 200)
           



    
             







    

    




