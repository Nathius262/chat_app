from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessageSerailizers, FriendSerializer
from .models import Message, Friend
from user.models import CustomUser as User
from rest_framework.viewsets import generics, mixins
from rest_framework.permissions import IsAuthenticated
import json


class MessageViewSets(generics.ListAPIView, mixins.RetrieveModelMixin):
    serializer_class = MessageSerailizers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = User.objects.get(username=self.request.user)
        return Message.objects.by_user(sender=request_user)

    def get(self, request):
        return self.list(request)
    
class FriendViewSet(generics.ListAPIView):
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Friend.objects.by_user(user=self.request.user).prefetch_related("message_receiver")
    
    def get(self, request):
                  
        return self.list(request)