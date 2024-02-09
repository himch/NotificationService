from django.db import models
from simple_history.models import HistoricalRecords

from NotificationService.settings import SMS_STATUS
from campaigns.models import Campaign
from clients.models import Client


STATUSES = tuple(zip(SMS_STATUS.values(), SMS_STATUS.values()))


class Sms(models.Model):
    time_create = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, choices=STATUSES, default='draft')
    campaign = models.ForeignKey(Campaign, related_name='sms', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='sms', on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'Client id: {self.id}, time_create: {self.time_create}, status: {self.status}'
