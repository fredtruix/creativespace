from .models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserRegisterForm(UserCreationForm):
  
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['avatar', 'username', 'first_name','last_name', 'email', 'bio',
        'instagram', 'linkedin', 'twitter']




# 