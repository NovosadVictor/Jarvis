from django import forms
from .models import Home, Room, Device


class InsertRoomForm(forms.ModelForm):
    room_name = forms.CharField(max_length=64)

    class Meta:
        model = Room
        fields = ['room_name']


class InsertDeviceForm(forms.ModelForm):
    device_name = forms.CharField(max_length=128)
    description = forms.CharField(max_length=1024)

    class Meta:
        model = Device
        fields = ['device_name', 'description']


class UpdateValuesForm(forms.ModelForm):
    mode = forms.BooleanField()

    class Meta:
        model = Device
        fields = ['mode', 'value']