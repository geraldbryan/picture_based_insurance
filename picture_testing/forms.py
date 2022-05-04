from django import forms
from models import *
from django.db.models import fields
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PersonalityForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','farmer_id']