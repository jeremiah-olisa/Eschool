from django.urls import path
from .views import *

app_name = 'forum'

urlpatterns = [
    path('', index, name='index'),
    path('sendMSG/', addForumForm, name='addForumForm'),
]

