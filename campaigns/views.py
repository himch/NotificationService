from rest_framework import generics

from campaigns.models import Campaign
from campaigns.serializers import CampaignSerializer, CampaignStatisticSerializer


class CampaignListAPIView(generics.ListCreateAPIView):
    """
        Returns a list of all campaigns in the system,
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Returns campaign details
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignCommonStatisticAPIView(generics.ListAPIView):
    """
        Returns a list of all campaigns in the system,
        including general statistics on created mailing lists
        and the number of messages sent to them, grouped by status
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignStatisticSerializer


class CampaignStatisticAPIView(generics.RetrieveAPIView):
    """
        Returns a campaign with number of messages sent to them, grouped by status
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignStatisticSerializer
