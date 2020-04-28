from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('profile/Submit/', ProfileFormValidator, name='ProfileFormValidator'),
    path('manual/', manual, name='manual'),
    path('report-bug/', reportBug, name='reportBug'),
    path('add/bug', addBugsForm, name='addBugsForm'),
]
