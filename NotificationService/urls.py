"""
URL configuration for NotificationService project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from campaigns.views import CampaignListAPIView, CampaignDetailAPIView, CampaignStatisticAPIView, \
    CampaignCommonStatisticAPIView, CampaignPausedOnAPIView, CampaignPausedOffAPIView
from clients.views import ClientListAPIView, ClientDetailAPIView
from sms.views import SmsListAPIView, SmsDetailAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/campaigns/', CampaignListAPIView.as_view(), name='campaign-list'),
    path('api/v1/campaigns/<int:pk>/', CampaignDetailAPIView.as_view(), name='campaign-detail'),
    path('api/v1/campaigns/<int:pk>/paused_on', CampaignPausedOnAPIView.as_view(), name='campaign-paused-on'),
    path('api/v1/campaigns/<int:pk>/paused_off', CampaignPausedOffAPIView.as_view(), name='campaign-paused-off'),
    path('api/v1/campaigns/statistic/', CampaignCommonStatisticAPIView.as_view(), name='campaign-common-statistic'),
    path('api/v1/campaigns/statistic/<int:pk>/', CampaignStatisticAPIView.as_view(), name='campaign-detail-statistic'),

    path('api/v1/clients/', ClientListAPIView.as_view(), name='client-list'),
    path('api/v1/clients/<int:pk>/', ClientDetailAPIView.as_view(), name='client-detail'),

    path('api/v1/sms/', SmsListAPIView.as_view(), name='sms-list'),
    path('api/v1/sms/<int:pk>/', SmsDetailAPIView.as_view(), name='sms-detail'),
]
