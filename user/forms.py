from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={'required': 'Email is required'})
    password = forms.CharField(error_messages={'required': 'Password is required'})

    def clean_password(self):
        data = self.cleaned_data["password"]
        try:
            # Check validation with rules here:
            # funny_movies/settings.py#L94
            password_validation.validate_password(data)
        except ValidationError as error:
            self.add_error("password", error)
        return data