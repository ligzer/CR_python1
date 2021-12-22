from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate, APIRequestFactory
from rest_framework import status
from .models import Store, Schedule
from django.db.models import Max
from django.contrib.auth.models import User


class CRUD_Tests(TestCase):
    """
    """

    def setUp(self):
        self.client = APIClient()
        user, created = User.objects.get_or_create(username='root')
        self.client.force_authenticate(user=user)

    def test_creation(self):
        """
        случай корректного запроса POST /api/store
        """

        request_json = \
            {
                "Name": "extend interactive networks",
                "Comment": "Re-contextualized system-worthy structure",
                "Town": "Sanchezberg",
                "Street": "Ruth Neck",
                "Number": "14817",
                "Schedule": [
                    {
                        "DayOfWeek": 1,
                        "OpenTime": "10:15:00",
                        "CloseTime": "18:00:00"
                    },
                    {
                        "DayOfWeek": 2,
                        "OpenTime": "09:30:00",
                        "CloseTime": "12:20:00"
                    },
                ]}
        response = self.client.post('/api/store/', request_json, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data, "Некорректный ответ сервера")
        store = Store.objects.get(pk=response.data["id"])
        self.assertEqual(2, store.Schedule.count(), 'No correct Schedule')
