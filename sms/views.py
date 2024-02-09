from rest_framework import generics

from sms.models import Sms
from sms.serializers import SmsSerializer


class SmsListAPIView(generics.ListCreateAPIView):
    """
        Returns a list of all sms messages in the system
    """
    queryset = Sms.objects.all()
    serializer_class = SmsSerializer


class SmsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Returns sms message details
    """
    queryset = Sms.objects.all()
    serializer_class = SmsSerializer
