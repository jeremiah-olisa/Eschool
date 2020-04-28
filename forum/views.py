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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from core.models import *
from core.forms import *

from .models import *
from .forms import *
		
# Create your views here.
@login_required
def index(request):
	try:
		profileData = Profile.objects.get(displayName=request.user)
	except ObjectDoesNotExist:
		profileData = []
		messages.info(request, "Please Create a Profile")
	username = str(request.user)
	forumData = Forum.objects.all().order_by("-id")
	forumDataReverse = forumData.reverse()
	#request for page query
	page = request.GET.get('page')
	#paginate by 30 messages
	paginator = Paginator(forumDataReverse, 3)
	try:
		forumDataReverse = paginator.page(page)
	except PageNotAnInteger:
		forumDataReverse = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {
		'profileData': profileData,
		'username': username,
		'forumData': forumDataReverse,
		'forumForm': ForumForm,
		'title': 'Forum',
		'pages': paginator.num_pages,
	}
	return render(request, "forum.html", context)

@login_required
def addForumForm(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
        else:
        	messages.error(request, "Please Fill All The Fields")
    else:
    	messages.error(request, "Something Went Wrong")
    return redirect('forum:index')
