from django.db import models

from NotificationService.settings import SMS_STATUS


class Campaign(models.Model):
	time_start = models.DateTimeField()
	time_finish = models.DateTimeField()
	text = models.CharField(max_length=160)
	filters = models.JSONField(max_length=100, default='{}')
	paused = models.BooleanField(default=False)

	@property
	def sms_draft_count(self):
		return self.sms.filter(status=SMS_STATUS['draft']).count()

	@property
	def sms_success_count(self):
		return self.sms.filter(status=SMS_STATUS['success']).count()

	@property
	def sms_error_count(self):
		return self.sms.filter(status=SMS_STATUS['error']).count()

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f'Campaign id: {self.id}, text: {self.text}, time_start: {self.time_start}, time_finish: {self.time_finish}'
