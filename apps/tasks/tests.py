from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.task = Task.objects.create(title='Test Task', user=self.user)

    def test_list_tasks(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post(reverse('task-list'), {'title': 'New Task', 'completed': False})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        response = self.client.put(reverse('task-detail', args=[self.task.id]), {'title': 'Updated Task', 'completed': True})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        response = self.client.delete(reverse('task-detail', args=[self.task.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
