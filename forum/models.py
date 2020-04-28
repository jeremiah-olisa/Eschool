from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

class Forum(models.Model):
	user = models.CharField(max_length=100)
	message = models.CharField(max_length=10000)
	date = models.DateTimeField(auto_now_add=True)