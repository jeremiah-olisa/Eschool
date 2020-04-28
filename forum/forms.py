from django import forms

from .models import *

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ('message','user')