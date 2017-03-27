#-*- coding: utf-8 -*-
from django import forms
from .models import Home, Room, Device


class InsertRoomForm(forms.ModelForm):
    room_name = forms.CharField(max_length=64, label='Название комнаты')

    class Meta:
        model = Room
        fields = ['room_name']


class InsertDeviceForm(forms.ModelForm):
    device_name = forms.CharField(max_length=128, label='Название прибора')
    description = forms.CharField(max_length=1024, label='Описание', help_text='необязательное поле', required=False)
    quantity = forms.IntegerField(label='Количество', help_text='необязательное поле', required=False)

    class Meta:
        model = Device
        fields = ['device_name', 'description', 'quantity']


class UpdateValuesForm(forms.ModelForm):
    mode = forms.BooleanField(label='Вкл/Выкл', required=False)
    value = forms.IntegerField(label='Показатели', required=False)

    class Meta:
        model = Device
        fields = ['mode', 'value']