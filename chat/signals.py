from .models import Message, Friend
from user.models import GroupPaticipant, CustomUser, CustomGroup
from django.db.models.signals import pre_save
from rest_framework import exceptions

def checkMessage(sender, instance, *args, **kwargs):
    
    try:
        user = CustomUser.objects.get(username=instance.sender)
        friend = CustomUser.objects.get(username=instance.receiver)
        Friend.objects.all().filter(user=user, friend=friend).exists()
    except CustomUser.DoesNotExist:    
        try:
            group = CustomGroup.objects.get(name=instance.receiver)
            GroupPaticipant.objects.all().filter(group=group, user=user).exists()
        except CustomGroup.DoesNotExist:
            raise exceptions.ValidationError(f'friends with {instance.message} or group does not exist')


pre_save.connect(checkMessage, sender=Message)