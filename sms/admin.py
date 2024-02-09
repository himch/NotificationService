from django.contrib import admin

from sms.models import Sms


@admin.register(Sms)
class SmsAdmin(admin.ModelAdmin):
    pass
