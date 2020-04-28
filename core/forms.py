from django import forms
from .models import Bug

yesOrNo = (
			('Yes', ('Yes')), 
			('No', ('No'))
		  )
role = (
			('Student', ('Student')), 
			('Teacher', ('Teacher')),
			('Parent', ('Parent')),
			('User', ('User')),
		  )
department = (
			('Science', ('Science')), 
			('Art', ('Art')),
			('Commercial', ('Commercial')),
			('Other', ('Other')),
		  )
grade = (
			('SS1', ('SS1')), 
			('SS2', ('SS2')),
			('SS3', ('SS3')),
			('Other', ('Other')),
		  )
disability = (
			('None', ('None')),
			('Dumb', ('Dumb')), 
			('Deaf', ('Deaf')),
			('Other', ('Other')),
		  )
class ProfileDetailForm(forms.Form):
	email = forms.CharField(max_length = 100,
								widget = forms.EmailInput(attrs = {
								'class' : "form-control",
								'name' : 'email' ,
						}))

	role = forms.ChoiceField(label=('Role'),choices = role)

	department = forms.ChoiceField(label=('Department'),choices = department)

	dob = forms.CharField(max_length = 100,
								widget = forms.DateInput(attrs = {
								'class' : "form-control",
								'name' : 'dob' ,
								'type' : 'date' ,
						}))
	
	showDOB = forms.ChoiceField(label=('showDOB'),choices = yesOrNo)
	
	grade = forms.ChoiceField(label=('Class'),choices = grade)
	
	phone = forms.CharField(max_length = 100,
								widget = forms.NumberInput(attrs = {
								'class' : "form-control",
								'name' : 'phone' ,
						}))
	
	showPhone = forms.ChoiceField(label=('showPhone'),choices = yesOrNo)
	
	fullName = forms.CharField(max_length = 100,
								widget = forms.TextInput(attrs = {
								'class' : "form-control",
						}))	

	address = forms.CharField(max_length = 100,
								widget = forms.TextInput(attrs = {
								'class' : "form-control",
						}))	

	state = forms.CharField(max_length = 100,
								widget = forms.TextInput(attrs = {
								'class' : "form-control",
						}))	

	country = forms.CharField(max_length = 100,
								widget = forms.TextInput(attrs = {
								'class' : "form-control",
						}))	

	disability = forms.ChoiceField(label=('Disability'),choices = disability)	

	profile = forms.CharField(max_length = 100,
								widget = forms.Textarea(attrs = {
								'class' : "form-control",
						}))	

	displayImage = forms.FileField(max_length = 100,
								widget = forms.FileInput(attrs = {
								'class' : "form-control",
						}))


class BugsForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('full_name', 'url', 'description')