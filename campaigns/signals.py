from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from campaigns.models import Campaign


@receiver(post_save, sender=Campaign)
def save_handler(sender, instance, created, **kwargs):
    time_start = instance.time_start
    time_finish = instance.time_finish
    if time_start <= timezone.now() <= time_finish:
        print('start now')
    else:
        print('plan to start')
