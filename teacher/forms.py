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
        fields = ("picture","phone_number", "application_letter", "years_of_experience", "qualifications", "cv")
        

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","first_name", "last_name", "email")