from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(help_text='enter your first name',label="firstname")
    last_name = forms.CharField(help_text='enter your last name')
    email_address = forms.CharField(help_text='enter your email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email_address', 'password1', 'password2', )