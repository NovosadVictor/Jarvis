from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import Http404
from .forms import InsertHomeForm
from homes.models import Home


def insert_home(request, pk):
    args = {}
    form = InsertHomeForm()
    try:
        user = User.objects.get(pk=pk)
        args['user'] = user
        if request.POST:
            home_form = InsertHomeForm(request.POST)
            if home_form.is_valid():
                house_keeper = user
                home_name = home_form.cleaned_data['home_name']
                address = home_form.cleaned_data['address']
                new_home = Home.objects.create(house_keeper=house_keeper, home_name=home_name, address=address);
                new_home.save()
                return redirect('/user/user_page/%d' % user.id)
            else:
                args['logic_error'] = 'There are something wrong'
        else:
            args['form'] = form
    except User.DoesNotExist():
        args['logic_error'] = 'There are no such user'
        raise Http404
    return render(request, 'users/insert_home.html', args)


def user_page_detail(request, pk):
    args = {}
    try:
        user = User.objects.get(pk=pk)
        if request.user == user:
            homes = user.home_set.all()
            args['user'] = user
            args['homes'] = homes
        else:
            args['logic_error'] = 'You cant be here'
    except User.DoesNotExist:
        args['logic_error'] = 'There are no such users'
        raise Http404
    return render(request, 'users/user_page.html', args)


