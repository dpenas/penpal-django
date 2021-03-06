import json

from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import User
from rest_framework.test import APIRequestFactory

class UserTestCase(APITestCase):
	def setUp(self):
		user = User(name="johndoe", email="john@email.com")
		user.save()

	def test_get_users(self):
		factory = APIRequestFactory()
		url = reverse('user_list')
		response = self.client.get(url, format="json")

		assert response.status_code == 200

		content = json.loads(response.content)

		self.assertEqual(len(content), 1)

		user_data = content[0]

		self.assertEqual(user_data['name'], 'johndoe')
		self.assertEqual(user_data['email'], 'john@email.com')

	def test_post_user(self):
		factory = APIRequestFactory()
		url = reverse('user_list')
		data = {'name': 'dario', 'email': 'dario@dario.com'}
		response = self.client.post(url, data, format="json")

		assert response.status_code == 201

		content = json.loads(response.content)

		self.assertEqual(content['name'], 'dario')
		self.assertEqual(content['email'], 'dario@dario.com')