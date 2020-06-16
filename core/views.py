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
from django.contrib import auth
from django.contrib.auth.models import User


from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.palettes import Spectral6


from .models import *
from .forms import *

from quiz.models import *
from notification.models import *

@login_required 
def index(request):
	user = User.objects.all()
	
	testData = Quiz.objects.all()
	notificationData = Notification.objects.filter(dontDisplay=False)
	userName = request.user
	progress, c = Progress.objects.get_or_create(user=userName)
	progressCategory = progress.list_all_cat_scores
	progressExams = progress.show_exams()

	test_name = []
	score = []
	progressData = []
	total = {}
	
	for x in progressExams:
		progressData.append(x.quiz.title)
		progressData.append(x.get_percent_correct)
		if x.quiz.title not in test_name:
			test_name.append(x.quiz.title)
	for index in range(0, len(progressData), 2):
	    if not progressData[index] in total:
	        total[progressData[index]] = progressData[index + 1]
	    else:
	        total[progressData[index]] += progressData[index + 1]
	for testName in test_name:
		countNumofTimesTestWasTaken = progressData.count(testName)
		avgScore = int(total[testName]/countNumofTimesTestWasTaken)
		score.append(avgScore)

	test_name_ranged = test_name[:6]
	score_ranged = score[:6]
	p = figure(x_range=test_name_ranged, plot_height=450, title='Personal Progress', toolbar_location='below', tools='pan,wheel_zoom,box_zoom,reset,hover,tap,crosshair')

	source = ColumnDataSource(data=dict(test_name=test_name_ranged, score=score_ranged, color=Spectral6))
	p.vbar(x=test_name_ranged, top=score_ranged, width=0.9, color=Spectral6)
	p.y_range.start = 0
	script, div = components(p) 

	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'title': 'Home',
		'script': script,
		'div': div,
		'totalNumOfTests': len(testData),
		'totalNumOfUsers': len(user),
		'totalNumOfTestTaken': 0,
		'numOfNotifiacation': len(notificationData),
		'profileData': profileData,
	}
	return render(request, "index.html", context) 

@login_required 
def profile(request):
	profileData = ProfileDetailForm
	displayFormStyle = "Block"
	displayProfileStyle = "None"
	try:
		profileData = Profile.objects.get(displayName=request.user)
		displayFormStyle = "None"
		displayProfileStyle = "Block"
	except ObjectDoesNotExist:
		messages.info(request, "Please Create a Profile")
	context = {
		'title': 'Profile',
		'profileData': profileData,
		'displayFormStyle': displayFormStyle,
		'displayProfileStyle': displayProfileStyle,
	}
	return render(request, "profile.html", context)

@login_required
def ProfileFormValidator(request):
    form = ProfileDetailForm(request.POST)
    if request.method == 'POST':
        profile = Profile(
            email = form.data['email'],
            role = form.data['role'],
            department = form.data['department'],
            dob = form.data['dob'],
            showDOB = form.data['showDOB'],
            grade = form.data['grade'],
            phone = form.data['phone'],
            showPhone = form.data['showPhone'],
            fullName = form.data['fullName'],
            address = form.data['address'],
            state = form.data['state'],
            country = form.data['country'],
            disability = form.data['disability'],
            profile = form.data['profile'],
            slug = request.user.id,
            displayName = request.user,
        )
        profile.save()
        success_msg = messages.add_message(request, messages.SUCCESS, f"Profile Set")
    else:
        success_msg = messages.add_message(request, messages.ERROR, f"Profile Not Set Try Again")
    return redirect("core:profile")

@login_required 
def base(request):
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'profileData': profileData,
	}
	return render(context)

def manual(request):
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'profileData': profileData,
		'title': 'Manual',
	}
	return render(request, "manual.html", context)

def reportBug(request):
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'profileData': profileData,
		'title': 'Report Bug',
		'bugsForm': BugsForm,
	}
	return render(request, "report-bug.html", context)

def error_404(request, exception):
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	context = {
		'profileData': profileData,
		'title': 'Page Not Found',
	}
	return render(request, "404.html", context)

def addBugsForm(request):
    if request.method == 'POST':
        form = BugsForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        else:
        	messages.error(request, "Please Fill All The Fields")
    else:
    	messages.error(request, "Something Went Wrong")
    return redirect('core:index')
