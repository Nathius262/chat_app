from .models import Message, Friend
from user.models import GroupPaticipant, CustomUser, CustomGroup
from django.db.models.signals import pre_save
from rest_framework import exceptions
from django.db.models import Q

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


#pre_save.connect(checkMessage, sender=Message)

def createMessage(sender, instance, *args, **kwargs):
    user = instance.sender
    friend = Q(friend=instance.receiver.friend) | Q(friend=instance.receiver.user)
    print(friend)

    lookup1 = Q(user=user) & Q(friend=friend)
    lookup2 = Q(user=friend) & Q(friend=user)
    lookup = Q(lookup1 | lookup2)
    qs = Friend.objects.filter(lookup)
    if qs.exists():
        pass
    else:
        raise exceptions.ValidationError(f'{user} and ({instance.receiver.friend} or {instance.receiver.user}) are not friends')

def createFriend(sender, instance, *args, **kwargs):
    user = instance.user
    friend = instance.friend
    print(user, friend)
    if user == friend:
        raise exceptions.ValidationError(f"{user} and {friend} cannot be friends")

    lookup1 = Q(user=user) & Q(friend=friend)
    lookup2 = Q(user=friend) & Q(friend=user)
    lookup = Q(lookup1 | lookup2)
    qs = Friend.objects.filter(lookup)
    if qs.exists():
        raise exceptions.ValidationError(f"{user} and {friend} are already friends")

pre_save.connect(createMessage, sender=Message)
pre_save.connect(createFriend, sender=Friend)