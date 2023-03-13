from django.shortcuts import render
from .serializers import CustomGroupSerializers, GroupPaticipantSerializers
from .models import CustomGroup, GroupPaticipant
from rest_framework.response import Response
from rest_framework.viewsets import generics, mixins
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class CustomGroupViewSet(generics.ListAPIView):
    serializer_class = CustomGroupSerializers
    queryset = CustomGroup

    def get(self, request):
        return self.list(request)

class GroupPaticipationViewSet(generics.ListAPIView, mixins.RetrieveModelMixin):
    serializer_class = GroupPaticipantSerializers
    queryset = GroupPaticipant
    lookup_field='id'
    permission_classes =[IsAuthenticated]

    def get(self, request, id=None):
        print(request.user)
        return self.retrieve(request)