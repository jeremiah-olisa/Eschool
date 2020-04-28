from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import DetailView, ListView, View
from django.conf import settings
from django.core.files.storage import FileSystemStorage

import datetime

from core.models import *
from core.forms import *

from .models import *
from .forms import *
def hideNotification():
	notificationData = Notification.objects.filter(dontDisplay=False).order_by("-id")
	for notifications in notificationData:
		currentDate = datetime.date.today()
		dateUploaded = f"{notifications.date.month}/{notifications.date.day}/{notifications.date.year}"
		convertDateUploaded = datetime.datetime.strptime(dateUploaded, '%m/%d/%Y').date()
		duration = currentDate - convertDateUploaded
		strDuration = str(duration)
		if duration.days >= notifications.duration:
			notifications.dontDisplay = True
			notifications.save()
			

@login_required 
def index(request):
	hideNotification()
	notificationData = Notification.objects.filter(dontDisplay=False).order_by("-id")
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'title': 'Notifications',
		'profileData': profileData,
		'notificationData': notificationData,
	}
	return render(request, "notification.html", context) 

@staff_member_required 
def addNotification(request):
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'title': 'Create Notification',
		'profileData': profileData,
		'notificationForm': NotificationForm,
	}
	return render(request, "create-notification.html", context) 
@staff_member_required
def addNotificationForm(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
        	messages.error(request, "Please Fill All The Fields")
    else:
    	messages.error(request, "Something Went Wrong")
    return redirect('notification:index')
