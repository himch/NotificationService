from rest_framework import serializers

from sms.models import Sms


class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sms
        fields = '__all__'
