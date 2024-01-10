from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']