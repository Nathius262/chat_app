from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
import json

User = get_user_model

"""class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        await self.send({
            'type':"websocket.accept"
        })

    async def websocket_receive(self, event):
        print('received', event)

    async def websocket_disconnect(self, event):
        print('disconnected', event)"""


class ChatCosumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type':"connection_established",
            "message":"You are connected"
        }))