from rest_framework import serializers
from .models import Message, Friend
from user.models import CustomUser as User, CustomGroup as Group
import json

class MessagePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ['id']


class MessageSerailizers(serializers.ModelSerializer):
    sender = serializers.SerializerMethodField("get_sender")
    receiver = serializers.SerializerMethodField("get_receiver")
    
    class Meta:
        model = Message
        exclude = ['id',]

    def get_sender(self, obj):
        return str(obj.sender)
    
    def get_receiver(self, obj):
        return str(obj.receiver)
    
 

class FriendSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField("get_user")
    friend = serializers.SerializerMethodField("get_friend")
    message_receiver = MessageSerailizers(many=True)
    
    class Meta:
        model = Friend
        exclude = ['id',]

    def get_friend(self, obj):
        user = self.context['request'].user
        if obj.friend == user:
            obj.friend = obj.user
            obj.user = user
        friend = {
            "username":obj.friend.username,
            "picture":obj.friend.picture_url
        }
        return friend
    
    def get_user(self, obj):
        user = self.context['request'].user
        if obj.friend == user:
            obj.friend = obj.user
            obj.user = user
        user = {
            "username":obj.user.username,
            "picture":obj.user.picture_url
        }
        return user