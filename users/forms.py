from django import forms
from homes.models import Home


class InsertHomeForm(forms.ModelForm):
    address = forms.CharField(max_length=256)#, blank=True, null=True)

    class Meta:
        model = Home
        fields = ['address']