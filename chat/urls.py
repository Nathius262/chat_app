from django.urls import path
from .views import MessageViewSets


app_name = 'chat'

urlpatterns = [
    path('', MessageViewSets.as_view())
]