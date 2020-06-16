from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
	email = models.CharField(max_length=100)
	role = models.CharField(max_length=50) 
	department = models.CharField(max_length=100)
	dob = models.DateField()
	showDOB = models.CharField(max_length=50) 
	grade = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	showPhone = models.CharField(max_length=50)
	fullName = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	disability = models.CharField(max_length=100)
	profile = models.TextField()
	slug = models.SlugField() 
	displayName = models.CharField(max_length=100)

	def __str__(self):
		return self.user

class Bug(models.Model):
	full_name = models.CharField(max_length=100)
	url = models.CharField(max_length=500,help_text=("Link of the Page Error occured. Copy the link where the Error Occured from your browser address bar"))
	description = models.TextField()
	def __str__(self):
		return f'{self.full_name} reported a bug @ {self.url}'