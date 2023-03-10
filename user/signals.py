from django.db.models.signals import post_save
from .models import GroupPaticipant, CustomGroup


def create_group_paticipant(sender, instance, *args, **kwargs):
    paticipant_admin = GroupPaticipant.objects.all().get_or_create(group=instance, user=instance.user, is_admin=True)
    return paticipant_admin

post_save.connect(create_group_paticipant, sender=CustomGroup)