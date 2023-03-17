from django.db import models
from django.conf import settings
from django.db.models import Q


class FriendManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(user=user) | Q(friend=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs


class Friend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False, related_name="friend_user")
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False, related_name="user_friend")
    friend_update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = FriendManager()

    class Meta:
        unique_together = ['user', 'friend']
        ordering = (
            '-friend_update',
            '-timestamp'
        )

    def __str__(self):
        return f"{self.user} with {self.friend}"

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_message")
    receiver = models.ForeignKey(Friend, on_delete=models.CASCADE, null=False, blank=False, related_name="message_receiver")
    message = models.TextField(max_length=50000, blank=False, null=True)
    message_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (
            '-message_date',
        )

    def __str__(self):
        return str(self.sender)