from django.db import models

from NotificationService.settings import SMS_STATUS


class Campaign(models.Model):
	time_start = models.DateTimeField()
	time_finish = models.DateTimeField()
	text = models.CharField(max_length=160)
	filter = models.CharField(max_length=100)

	@property
	def sms_draft_count(self):
		return self.sms.filter(id=self.id, status=SMS_STATUS['draft']).count()

	@property
	def sms_success_count(self):
		return self.sms.filter(id=self.id, status=SMS_STATUS['success']).count()

	@property
	def sms_error_count(self):
		return self.sms.filter(id=self.id, status=SMS_STATUS['error']).count()

	class Meta:
		ordering = ['id']

	def __str__(self):
		return f'Campaign id: {self.id}, text: {self.text}, time_start: {self.time_start}, time_finish: {self.time_finish}'
