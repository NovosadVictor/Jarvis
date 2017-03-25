from django import forms
from homes.models import Home


class InsertHomeForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = ['home_name','address']