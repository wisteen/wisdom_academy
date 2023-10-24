from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("category","picture","phone_number", "application_letter", "years_of_experience", "qualifications", "cv")
        

class RegistrationForm(UserCreationForm):
	username = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Your Username'}))
	email = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Enter your email'}))
	first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Last Name'}))
	password1 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
	class Meta:
		model = User
		fields = ("username","first_name", "last_name", "email")
