from django.urls import path
from django.conf.urls import re_path
from .consumers import ChatConsumer


websocket_urlpatterns = [
    re_path('chat/', ChatConsumer.as_asgi()),
]
