from django.contrib import admin
from .models import Message, Friend

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_to', 'message_date']
    list_filter = ['user', 'message_to']

class FriendAmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Friend, FriendAmin)
admin.site.register(Message, MessageAdmin)