from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


class Client(models.Model):
	phone = PhoneNumberField(null=False, blank=False, unique=True)
	op_code = models.CharField(max_length=3)
	tag = models.CharField(max_length=100)
	timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')

	def __str__(self):
		return f'Client id: {self.id}, phone: {self.phone}'
