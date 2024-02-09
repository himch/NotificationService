from rest_framework import generics

from clients.models import Client
from clients.serializers import ClientSerializer


class ClientListAPIView(generics.ListCreateAPIView):
    """
        Returns a list of all clients in the system
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
        Returns client details
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
