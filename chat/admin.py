from django.contrib import admin
from .models import Message, Friend
from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError

# Register your models here.
admin.site.register(Message)


class Message(admin.StackedInline):
    model = Message
    

class MessageForm(forms.ModelForm):
    def clean(self):
        super(MessageForm, self).clean()
        user = self.cleaned_data.get('user')
        friend = self.cleaned_data.get('friend')

        lookup1 = Q(user=user) & Q(friend=friend)
        lookup2 = Q(user=friend) & Q(friend=user)
        lookup = Q(lookup1 | lookup2)
        qs = Friend.objects.filter(lookup)
        if qs.exists():
            raise ValidationError(f"{user} and {friend} are already friends")

class FriendAmin(admin.ModelAdmin):
    inlines = [Message,]
    #form = MessageForm
    list_display = ['user', 'friend']

    class Meta:
        model = Friend


admin.site.register(Friend, FriendAmin)
