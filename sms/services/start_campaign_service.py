import json

from django.utils import timezone
from django.db.models import Q
from NotificationService.settings import SMS_STATUS
from clients.models import Client
from sms.services.send_sms_service import SendSmsService


class StartCampaignService:
    def create_messages(self, campaign):
        # create messages for campaign
        filters = json.loads(campaign.filters)
        if filters:
            if 'op_codes' in filters:
                pass
            if 'tags' in filters:
                pass
            clients = Client.objects.all()

    def execute(self, campaign):
        self.create_messages()
        not_sent_messages = campaign.sms.filter(~Q(status=SMS_STATUS['success']))
        print(not_sent_messages.count())
        print(campaign.time_finish)
        print(timezone.now())
        while not_sent_messages.count() > 0 and campaign.time_finish >= timezone.now():
            for message in not_sent_messages:
                print(message.phone)
                SendSmsService().execute(sms_id=message.id,
                                         phone=message.id,
                                         text=message.text)


def test_start_campaign():
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NotificationService.settings')
    import django
    django.setup()
    from campaigns.models import Campaign
    campaign = Campaign.objects.all().first()
    print(StartCampaignService().execute(campaign))


if __name__ == '__main__':
    test_start_campaign()
