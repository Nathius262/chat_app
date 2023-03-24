from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import MessagePostSerializer, MessageSerailizers, FriendSerializer
from .models import Message, Friend
from user.models import CustomUser as User
from rest_framework.viewsets import generics, mixins
from rest_framework.permissions import IsAuthenticated
import json


class MessageViewSets(generics.ListAPIView, mixins.RetrieveModelMixin, mixins.CreateModelMixin):
    serializer_class = MessagePostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        friend = User.objects.get(username=request.data['receiver'])
        user = User.objects.get(username=request.data['sender'])
        request.data['receiver'] = Friend.objects.get(user=user, friend=friend).all().first().id
        request.data['sender'] = user.id
        return self.create(request)
    
class FriendViewSet(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = FriendSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Friend.objects.by_user(user=self.request.user).order_by("-friend_update").prefetch_related("message_receiver")
    
    def get(self, request):
        return self.list(request)