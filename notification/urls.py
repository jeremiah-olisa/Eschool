from django.urls import path
from .views import *

app_name = 'notification'

urlpatterns = [
    path('', index, name='index'),
    path('createNotification/', addNotification, name='addNotification'),
    path('add/', addNotificationForm, name='addNotificationForm'),
]