from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/home2/')
        self.assertEqual(response.status_code, 200)

    def test_url_name_exists(self):
        response = self.client.get(reverse('home2'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/home2/')
        self.assertTemplateUsed(response, 'testapp/home2.html')
        self.assertTemplateUsed(response, 'testapp/base.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('/home2/')
        print(response)
        self.assertContains(response, "Welcome to the homepage!")
        self.assertIn(b'Welcome to the homepage!', response.content)





class AboutPageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about2/')
        self.assertEqual(response.status_code, 200)

    def test_url_name_exists(self):
        response = self.client.get(reverse('about2'))
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_template(self):
        response = self.client.get('/about2/')
        self.assertTemplateUsed(response, 'testapp/about2.html')

    def test_aboutpage_contains_correct_html(self):
        response = self.client.get('/about2/')
        self.assertContains(response, "About us page!")
