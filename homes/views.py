from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import Http404
from .models import Home, Room, Device
from .forms import InsertRoomForm, InsertDeviceForm, UpdateValuesForm


def home_page_detail(request, pk, home_id):
    args = {}
    try:
        user = User.objects.get(pk=pk)
        if request.user == user:
            home = user.home_set.get(id=home_id)
            rooms = home.room_set.all()
            args['user'] = user
            args['home'] = home
            args['rooms'] = rooms
        else:
            args['logic_error'] = 'You cant be here'
    except User.DoesNotExist:
        args['logic_error'] = 'There are no such user or home'
        raise Http404
    return render(request, 'homes/homes_page.html', args)


def room_detail(request, home_id, room_id):
    args = {}
    try:
        home = Home.objects.get(id=home_id)
        room = home.room_set.get(id=room_id)
        devices = room.device_set.all()
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
        args['user'] = home.house_keeper
        if request.POST:
            room_form = InsertRoomForm(request.POST)
            if room_form.is_valid():
                name = room_form.cleaned_data['room_name']
                new_room = Room.objects.create(home=home, room_name=name)
                new_room.save()
                args['success'] = 'Вы успешно добавили комнату'
                return render('/homes/%d/' % home.house_keeper + 'homes_page/%d' % home.id)
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
        args['home'] = room.home
        if request.POST:
            device_form = InsertDeviceForm(request.POST)
            if device_form.is_valid():
                name = device_form.cleaned_data['device_name']
                description = device_form.cleaned_data['description']
                quantity = device_form.cleaned_data['quantity']
                new_device = Device.objects.create(
                    room=room,
                    device_name=name,
                    description=description,
                    quantity=quantity
                )
                new_device.description = request.POST['description']
                new_device.save()
                args['success'] = 'Вы успешно добавили прибор'
            else:
                args['logic_error'] = 'There are something wrong'
    except Room.DoesNotExist():
        args['logic_error'] = 'There are no such home'
        raise Http404
    args['form'] = form
    return render(request, 'homes/insert_device.html', args)


def update_values(request, device_id):
    args = {}
    form = UpdateValuesForm()
    try:
        device = Device.objects.get(id=device_id)
        args['device'] = device
        args['room'] = device.room
        args['home'] = device.room.home
        if request.POST:
            update_form = UpdateValuesForm(request.POST)
            if update_form.is_valid():
                mode = update_form.cleaned_data['mode']
                value = update_form.cleaned_data['value']
                device.value = value
                device.mode = mode
                device.save()
                return redirect('/homes/%d/' % device.room.home + 'room_page/%d' % device.room)
            else:
                args['logic_error'] = 'There are something wrong'
    except Device.DoesNotExist:
        args['logic_error'] = 'There are no such device'
        raise Http404
    args['form'] = form
    return render(request, 'homes/update_values.html', args)





