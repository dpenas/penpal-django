from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .serializers import UserSerializer, MessageSerializer
from .models import User, Message
from pprint import pprint

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)
 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all()
        
        messages_serializer = MessageSerializer(messages, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
 
    elif request.method == 'POST':
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data=message_data)
        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_received_message_list(request, user_id):
	messages = Message.objects.filter(to_user=user_id)
	messages_serializer = MessageSerializer(messages, many=True)

	return JsonResponse(messages_serializer.data, safe=False)

@api_view(['GET'])
def user_sent_message_list(request, user_id):
	messages = Message.objects.filter(from_user=user_id)
	messages_serializer = MessageSerializer(messages, many=True)

	return JsonResponse(messages_serializer.data, safe=False)