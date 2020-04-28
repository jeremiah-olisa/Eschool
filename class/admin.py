from django.contrib import admin
from .models import *

# Register your models here.
class ClassAdmin(admin.ModelAdmin):
	list_display = ('content',)

admin.site.register(Class, ClassAdmin)