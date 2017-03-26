from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=64, label='Логин')
    first_name = forms.CharField(required=False, label='Имя', help_text='необязательное поле')
    last_name = forms.CharField(required=False, label='Фамилия', help_text='необязательное поле')
    email = forms.EmailField(label='Емэйл')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Повторите пароль')