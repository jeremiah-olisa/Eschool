from django.urls import path

app_name = 'class'

from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('<slug>/', index),
    path('viewClass/<slug>/', viewClass, name='viewClass'),
    path(r'search/', search, name='search'),
]