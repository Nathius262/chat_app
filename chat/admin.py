from django.contrib import admin
from .models import Message, Friend

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'message_date']
    list_filter = ['sender', 'receiver']

class FriendAmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Friend, FriendAmin)
admin.site.register(Message, MessageAdmin)