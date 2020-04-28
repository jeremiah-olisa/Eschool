from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.views.generic import DetailView, ListView, View
from django.conf import settings

from core.models import *
from core.forms import *

from .models import *
from .forms import *
		
# Create your views here.
@login_required
def index(request, slug):
	classes = Class.objects.filter(subject=slug)
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'profileData': profileData,
		'title': slug.title,
		'classes': classes,

	}
	return render(request, "class.html", context)
@login_required
def viewClass(request, slug):
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	try:
		classes = Class.objects.get(id=slug)
	except ObjectValueError: 
		messages.info(request, "No material For This Class")
	context = {
		'profileData': profileData,
		'title': classes.topic.title,
		'content': classes,

	}

	return render(request, "view-class.html", context)


def search(request):
	query = request.GET.get('search')
	if query:
		qset = (
					Q(teacher_name__icontains=query) |
					Q(subject__icontains=query) |
					Q(content__icontains=query) |
					Q(topic__icontains=query) |
					Q(date__icontains=query)
				)
		results = Class.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response(
								"class.html", 
								{
									"classes": results,
									"title": f"Search {query}".title,
								}
							)