from django import forms
from homes.models import Home


class InsertHomeForm(forms.ModelForm):
    home_name = forms.CharField(max_length=128, label='Название дома')
    address = forms.CharField(max_length=256, label='Адрес', help_text='необязательное поле')

    class Meta:
        model = Home
        fields = ['home_name','address']