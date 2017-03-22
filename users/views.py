from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import Http404
from .forms import InsertHomeForm

def insert_home(request, pk):
    args = {}
    form = InsertHomeForm()
    try:
        user = User.objects.get(pk=pk)
        args['user'] = user
        if request.POST:
            home_form = InsertHomeForm(request.POST)
            if home_form.is_valid():
                home_form.save()
                house_keeper = user
                address = home_form.cleaned_data['address']
                new_home = Home.objects.create(house_keeper=house_keeper, address=address)
                new_home.save()
                args['success'] = 'success'
            else:
                args['logic_error'] = 'There are something wrong'
        else:
            args['form'] = form
    except User.DoesNotExist():
        args['logic_error'] = 'There are no such user'
        raise Http404
    return render(request, 'homes/insert_home.html', args)


def user_page_detail(request, pk):
    args = {}
    try:
        user = User.objects.get(pk=pk)
        homes = user.home_set()
        args['user'] = user
        args['homes'] = homes
    except User.DoesNotExist:
        args['logic_error'] = 'There are no such users'
        raise Http404
    return render(request, 'users/user_page.html', args)


