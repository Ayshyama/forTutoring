from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title="first todo", description="a description here")

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.title}"
        self.assertEqual(expected_object_name, "first todo")

    def test_description_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f"{todo.description}"
        self.assertEqual(expected_object_name, "a description here")

    def test_api_listview(self):
        response = self.client.get(reverse("todo_list"))
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "first todo")


    def test_api_detailview(self):
        response = self.client.get(reverse("todo_detail", args=[1]))
        # response = self.client.get(reverse("todo_detail", kwargs={'pk': self.todo.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "first todo")
        self.assertContains(response, "a description here")