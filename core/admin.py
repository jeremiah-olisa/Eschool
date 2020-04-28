from django.contrib import admin
from .models import *

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('fullName', 'phone', 'email', 'role', 'department','dob', 'grade', 'country')

class BugAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'url')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Bug, BugAdmin)