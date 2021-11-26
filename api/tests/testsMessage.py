import json

from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import User
from rest_framework.test import APIRequestFactory

class MessageTestCase(APITestCase):
	def setUp(self):
		user_john = User(name='johndoe', email='john@email.com')
		user_john.save()

		user_jane = User(name='janedoe', email='jane@email.com')
		user_jane.save()

	def test_send_message(self):
		factory = APIRequestFactory()
		url = reverse('message_list')
		user_sender = User.objects.get(email='john@email.com')
		user_receiver = User.objects.get(email='jane@email.com')

		data = {'from_user': user_sender.id, 'to_user': user_receiver.id, 'body': 'test'}
		response = self.client.post(url, data, format='json')

		assert response.status_code == 201

		content = json.loads(response.content)

		self.assertEqual(content['body'], 'test')
		self.assertEqual(content['to_user'], user_receiver.id)
		self.assertEqual(content['from_user'], user_sender.id)

	def test_message_received(self):
		factory = APIRequestFactory()
		user_sender = User.objects.get(email='john@email.com')
		user_receiver = User.objects.get(email='jane@email.com')
		url_send_message = reverse('message_list')
		url_message_received = reverse('messages_received', kwargs={'user_id':user_receiver.id})

		data = {'from_user': user_sender.id, 'to_user': user_receiver.id, 'body': 'This is a nice message'}
		self.client.post(url_send_message, data, format='json')

		response = self.client.get(url_message_received, format='json')

		assert response.status_code == 200

		content = json.loads(response.content)

		message_data = content[0]

		self.assertEqual(message_data['body'], 'This is a nice message')
		self.assertEqual(message_data['to_user'], user_receiver.id)
		self.assertEqual(message_data['from_user'], user_sender.id)

	def test_message_sent(self):
		factory = APIRequestFactory()
		user_sender = User.objects.get(email='john@email.com')
		user_receiver = User.objects.get(email='jane@email.com')
		url_send_message = reverse('message_list')
		url_message_sent = reverse('messages_sent', kwargs={'user_id':user_sender.id})

		data = {'from_user': user_sender.id, 'to_user': user_receiver.id, 'body': 'This is a great message'}
		self.client.post(url_send_message, data, format='json')

		response = self.client.get(url_message_sent, format='json')

		assert response.status_code == 200

		content = json.loads(response.content)

		message_data = content[0]

		self.assertEqual(message_data['body'], 'This is a great message')
		self.assertEqual(message_data['to_user'], user_receiver.id)
		self.assertEqual(message_data['from_user'], user_sender.id)