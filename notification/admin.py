from django.contrib import admin
from .models import *

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
	list_display = ('user', 'message', 'duration', 'priority', 'dontDisplay','date')
admin.site.register(Notification, NotificationAdmin)