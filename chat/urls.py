from django.urls import path
from .views import MessageViewSets, FriendViewSet


app_name = 'chat'

urlpatterns = [
    path('message/', MessageViewSets.as_view()),
    path('friend/', FriendViewSet.as_view())
]