from rest_framework import serializers

from campaigns.models import Campaign
from sms.serializers import SmsSerializer


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = "__all__"


class CampaignStatisticSerializer(serializers.ModelSerializer):
    sms = SmsSerializer(many=True, read_only=True)

    class Meta:
        model = Campaign
        fields = ("id",
                  'time_start',
                  'time_finish',
                  'text',
                  'filter',
                  'sms_draft_count',
                  'sms_success_count',
                  'sms_error_count',
                  'sms',
                  )

