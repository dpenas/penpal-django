from django.test import TestCase
from api.models import User
from rest_framework.test import APIRequestFactory
from pprint import pprint
from .views import UserViewSet

class UserTestCase(TestCase):
	def setUp(self):
		user = User(name="lion", email="roar@email.com")
		user.save()

	def test_get_users(self):
		factory = APIRequestFactory()
		request = factory.get('/users', format="json")
		response = UserViewSet.as_view({'get': 'list'})(request)
		users = response.data
		self.assertEqual(len(users), 1)

		user_values = list(users[0].items())
		name = user_values[0][1]
		email = user_values[1][1]
		
		self.assertEqual(name, 'lion')
		self.assertEqual(email, 'roar@email.com')
