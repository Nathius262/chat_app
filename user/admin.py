from django.contrib import admin
from django.contrib.auth.models import Group
from .models import CustomUser, CustomGroup, GroupPaticipant

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_admin']

class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date_created']

class GroupPaticipantAdmin(admin.ModelAdmin):
    list_display = ['group', 'user', 'date_joined', 'is_admin']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup, GroupAdmin)
admin.site.register(GroupPaticipant, GroupPaticipantAdmin)
admin.site.unregister(Group)