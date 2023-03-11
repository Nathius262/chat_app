
from django.urls import path
from .views import GroupPaticipationViewSet, CustomGroupViewSet

app_name = "user"

urlpatterns = [
    path('group/<int:id>/', GroupPaticipationViewSet.as_view(), name="group_paticipant"),
]