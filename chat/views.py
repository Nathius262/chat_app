from django.shortcuts import render
from .serializers import MessageSerailizers
from .models import Message
from user.models import CustomUser as User
from rest_framework.viewsets import generics, mixins
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404


class MessageViewSets(generics.ListAPIView, mixins.RetrieveModelMixin):
    serializer_class = MessageSerailizers
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request_user = User.objects.get(username=self.request.user)
        return self.queryset.filter(sender=request_user)

    def get(self, request):
        return self.list(request)