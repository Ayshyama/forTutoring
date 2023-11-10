from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse

# Create your tests here.
User = get_user_model()

class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        cls.post = Post.objects.create(
            title='Test title',
            body='Test body',
            author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'Test title')
        self.assertEqual(self.post.body, 'Test body')
        self.assertEqual(self.post.author, self.user)
