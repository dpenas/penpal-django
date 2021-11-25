from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api/messages$', views.message_list, name='message_list'),
    url(r'^api/users$', views.user_list, name='user_list'),
    url(r'^api/users/(?P<user_id>\d+)/messages/received$', views.user_received_message_list, name='messages_received'),
    url(r'^api/users/(?P<user_id>\d+)/messages/sent$', views.user_sent_message_list, name='messages_sent'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]