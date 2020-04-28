from django.contrib import admin
from .models import *

# Register your models here.
class ForumAdmin(admin.ModelAdmin):
	list_display = ('user', 'message', 'date')
admin.site.register(Forum, ForumAdmin)