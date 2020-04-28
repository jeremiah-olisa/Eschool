from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
PRIORITY_CHOICES = (
		('danger', ('Top Priority')),
		('warning', ('Middle Priority')),
		('success', ('Minor Priority')),
		('dark', ('Other')),
	)
class Notification(models.Model):
	user = models.CharField(max_length=100)
	message = models.CharField(max_length=100)
	priority = models.CharField(choices=PRIORITY_CHOICES, max_length=100)
	duration = models.IntegerField()
	dontDisplay = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
