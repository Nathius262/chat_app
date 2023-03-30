from django.urls import path
from .consumers import ChatConsumer

websocket_urlpartterns = [
    path('chat/', ChatConsumer.as_asgi()),
]