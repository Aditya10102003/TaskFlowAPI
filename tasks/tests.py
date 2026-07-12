from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task


class TaskAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.token}"
        )

    def test_create_task(self):
        data = {
            "title": "Learn Django Testing",
            "description": "Write unit tests",
            "status": "Pending",
            "priority": "High"
        }

        response = self.client.post("/api/tasks/", data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().title, "Learn Django Testing")
        
    def test_get_tasks(self):
        Task.objects.create(
            user=self.user,
            title="Task 1",
            description="Demo",
            status="Pending",
            priority="High"
        )

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_update_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Old Title",
            description="Demo",
            status="Pending",
            priority="High"
        )

        response = self.client.patch(
            f"/api/tasks/{task.id}/",
            {"status": "Completed"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        task.refresh_from_db()
        self.assertEqual(task.status, "Completed")


    def test_delete_task(self):
        task = Task.objects.create(
            user=self.user,
            title="Delete Me",
            description="Demo",
            status="Pending",
            priority="Low"
        )

        response = self.client.delete(f"/api/tasks/{task.id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)


    def test_unauthorized_access(self):
        self.client.credentials()

        response = self.client.get("/api/tasks/")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)