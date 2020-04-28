from django import forms
from .models import *

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('teacher_name', 'subject', 'topic', 'content', 'material')
