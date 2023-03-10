from django.db import models
from django.conf import settings

# Create your models here.
class Friend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=False, related_name="friend_user")
    friend = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.user)

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_message")
    receiver = models.CharField(max_length=500, blank=False, null=True)
    message = models.TextField(max_length=50000, blank=False, null=True)
    message_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (
            '-message_date',
        )

    def __str__(self):
        return str(self.user)