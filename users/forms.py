#-*- coding: utf-8 -*-
from django import forms
from homes.models import Home


class InsertHomeForm(forms.ModelForm):
    home_name = forms.CharField(max_length=128, label='Название дома')
    address = forms.CharField(max_length=256, label='Адрес', help_text='необязательное поле', required=False)

    class Meta:
        model = Home
        fields = ['home_name','address']