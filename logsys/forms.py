from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()#blank=True, null=True)
    last_name = forms.CharField()#blank=True, null=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']