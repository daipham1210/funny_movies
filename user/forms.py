from django.contrib.auth.forms import AuthenticationForm
from django import forms

class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
