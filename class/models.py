from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField
SUBJECT_CHOICES = (
		('agric', ('agric')),
		('biology', ('biology')),
		('civic', ('civic')),
		('english', ('english')),
		('math', ('math')),
		('ccp', ('ccp')),
		('dp', ('dp')),
		('economics', ('economics')),
		('ict', ('ict')),
		('accts', ('accts')),
		('chemistry', ('chemistry')),
		('commerce', ('commerce')),
		('fisheries', ('fisheries')),
		('f-math', ('f-math')),
		('f-nut', ('f-nut')),
		('government', ('government')),
		('literature', ('literature')),
		('physics', ('physics')),
	)
class Class(models.Model):
	teacher_name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100, choices=SUBJECT_CHOICES)
	content = models.TextField(default="Download the Material below")
	topic = models.CharField(max_length=100)
	material = CloudinaryField('material')
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.topic