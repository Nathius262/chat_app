from .models import Message, Friend
from django.db.models.signals import pre_save
from rest_framework import exceptions
from django.db.models import Q

def createMessage(sender, instance, *args, **kwargs):
    """
    this function is a signal sent to the Message model 
    for sender and receiver validation
    """
    user = instance.sender
    friend1 = instance.receiver.friend
    friend2 = instance.receiver.user

    # checking if the sender is in one of the friend 
    # instance else raise an error
    if user == friend1:
        friend = friend2
    elif user == friend2:
        friend = friend1
    else:
        raise exceptions.ValidationError(f'{user} and ({instance.receiver.friend} or {instance.receiver.user}) are not friends')
    
    #quering the sender and the receiver from the friend object 
    # if they exits else raise error
    lookup1 = Q(user=user) & Q(friend=friend)    
    lookup2 = Q(user=friend) & Q(friend=user)
    
    lookup = Q(lookup1 | lookup2)
    qs = Friend.objects.filter(lookup)
    
    if not(qs.exists()):
        raise exceptions.ValidationError(f'{user} and ({instance.receiver.friend} or {instance.receiver.user}) are not friends')

def createFriend(sender, instance, *args, **kwargs):
    
    """
    this function is a signal sent to the Friend model 
    to validation the user and friend before saving to the database.
    """

    user = instance.user
    friend = instance.friend
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