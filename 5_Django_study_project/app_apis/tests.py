from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from app_posts.models import Post

User = get_user_model()


class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            email='testuser@mail.com',
            password='testpass123')
        cls.admin_user = User.objects.create_superuser(
            username='adminuser',
            email='testadmin@mail.com',
            password='adminpass123')

        cls.post = Post.objects.create(
            title='Test title',
            body='Test body',
            author=cls.user)

        cls.post_list_url = reverse('post-list')
        cls.post_detail_url = reverse('post-detail', kwargs={'pk': cls.post.pk})

    def test_list_unauthenticated(self):
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_list_authenticated(self):
        self.client.login(
            username='testuser',
            password='testpass123')

        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

    def test_detail_authenticated_not_author(self):
        another_user = User.objects.create_user(
            username='anotheruser',
            email='anotheruser@mail.com',
            password='anotherpass123'
        )

        logged_in = self.client.login(
            username='anotheruser',
            password='anotherpass123'
        )
        print(logged_in)

        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)