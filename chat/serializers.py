from rest_framework import serializers
from .models import Message
from user.models import CustomUser as User


class MessageSerailizers(serializers.ModelSerializer):

    receiver = serializers.SerializerMethodField()
    
    class Meta:
        model = Message
        exclude = ['id',]


    def get_receiver(self, obj):
        receiver ={}

        try:
            user = User.objects.all().filter(username=obj.receiver).first()
            receiver = {
                "username":user.username,
                "picture": user.picture_url
            }
            #profile.append(receiver)
        except AttributeError:
            receiver = {
                "username":obj.receiver,
                "picture":'/media/default.png'
            }
            #profile.append(receiver)

        return receiver