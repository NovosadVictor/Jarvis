from django.shortcuts import render
from django.contrib.auth.models import User
from django.http.response import Http404
from .models import Home, Room, Device
from .forms import InsertRoomForm, InsertDeviceForm, UpdateValuesForm


def home_page_detail(request, pk, home_id):
    args = {}
    try:
        user = User.objects.get(pk=pk)
        home = user.home_set(id=home_id)
        args['user'] = user
        args['home'] = home
    except User.DoesNotExist:
        args['logic_error'] = 'There are no such user or home'
        raise Http404
    return render(request, 'homes/homes_page.html', args)


def room_detail(request, home_id, room_id):
    args = {}
    try:
        home = Home.objects.get(id=home_id)
        room = home.room_set(id=room_id)
        devices = room.device_set()
        args['home'] = home
        args['room'] = room
        args['devices'] = devices
    except Home.DoesNotExist:
        args['logic_error'] = 'There are no such home or room'
        raise Http404
    return render(request, 'homes/room_page.html', args)


def insert_room(request, home_id):
    args = {}
    form = InsertRoomForm()
    try:
        home = Home.objects.get(id=home_id)
        args['home'] = home
        if request.POST:
            room_form = InsertRoomForm(request.POST)
            if room_form.is_valid():
                room_form.save()
                name = room_form.cleaned_data['room_name']
                new_room = Room.objects.create(home=home, room_name=name)
                new_room.save()
                args['success'] = 'success'
            else:
                args['logic_error'] = 'There are something wrong'
        else:
            args['form'] = form
    except Home.DoesNotExist():
        args['logic_error'] = 'There are no such home'
        raise Http404
    return render(request, 'homes/insert_room.html', args)


def insert_device(request, room_id):
    args = {}
    form = InsertDeviceForm()
    try:
        room = Room.objects.get(id=room_id)
        args['room'] = room
        if request.POST:
            device_form = InsertDeviceForm(request.POST)
            if device_form.is_valid():
                device_form.save()
                name = device_form.cleaned_data['device_name']
                new_device = Device.objects.create(room=room, device_name=name)
                new_device.description = request.POST['description']
                new_device.save()
                args['success'] = 'success'
            else:
                args['logic_error'] = 'There are something wrong'
        else:
            args['form'] = form
    except Room.DoesNotExist():
        args['logic_error'] = 'There are no such home'
        raise Http404
    return render(request, 'homes/insert_device.html', args)


def update_values(request, device_id):
    args = {}
    form = UpdateValuesForm()
    try:
        device = Device.ogjects.get(id=device_id)
        args['device'] = device
        if request.POST:
            update_form = UpdateValuesForm(request.POST)
            if update_form.is_valid():
                update_form.save()
                mode = update_form.cleaned_data['mode']
                value = update_form.cleaned_data['value']
                device.value = value
                device.mode = mode
                device.save()
                args['success'] = 'success'
            else:
                args['logic_error'] = 'There are something wrong'
        else:
            args['form'] = form
    except Device.DoesNotExist:
        args['logic_error'] = 'There are no such device'
        raise Http404
    return render(request, 'homes/update_values.html', args)





