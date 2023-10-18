from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(title='My Test Post', body='This is a test post')

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        self.assertEqual(expected_title, 'My Test Post')
        self.assertEqual(expected_body, 'This is a test post')

    def test_url_exists_at_correct_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_url_available_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_template_name_is_correct(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'testapp/home.html')