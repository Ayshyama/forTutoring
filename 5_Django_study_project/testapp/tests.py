from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.


class HomePageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_url_name_exists(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'testapp/home.html')
        self.assertTemplateUsed(response, 'testapp/base.html')

    def test_homepage_contains_correct_html(self):
        response = self.client.get('')
        print(response)
        self.assertContains(response, 'Home Page')
        self.assertIn(b'Home Page', response.content)


class AboutPageTests(SimpleTestCase):
    def test_url_exists(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_url_name_exists(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_aboutpage_template(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'testapp/about.html')
        self.assertTemplateUsed(response, 'testapp/base.html')


