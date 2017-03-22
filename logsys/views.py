from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm


def main_page(request):
    args = {}
    args['user_bool'] = False
    args['logic_error_bool'] = False
    args['success_bool'] = False
    return render(request, 'logsys/main_page.html')


def user_login(request):
    args = {}
    args['user_bool'] = False
    args['logic_error_bool'] = False
    args['success_bool'] = False
    form = LoginForm()
    if request.POST:
        new_form = LoginForm(request.POST)
        if new_form.is_valid():
            new_form.save()
            username = new_form.cleaned_data['username']
            password = new_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                args['user'] = user
                args['user_bool'] = True
                args['success'] = 'success'
                args['success_bool'] = True
                return render(request, 'logsys/main_page.html', args)
            else:
                args['logic_error'] = 'There are no such users'
                args['logic_error_bool'] = True
        else:
            args['logic_error'] = 'Something worng'
            args['logic_error_bool'] = True
    else:
        args['form'] = form
    return render(request, 'logsys/login_page.html', args)


def user_logout(request):
    if request.user.is_authenticated():
        logout(request)
        return redirect('/')
    else:
        logic_error = 'How did you do it?'
        return render(request, 'logsys/main_page.html', {'logic_error': logic_error})


def user_registration(request):
    args = {}
    args['user_bool'] = False
    args['logic_error_bool'] = False
    args['success_bool'] = False
    form = RegistrationForm()
    if request.POST:
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            email = user_form.cleaned_data['email']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(user, request)
            args['user'] = user
            args['user_bool'] = True
            args['success'] = 'success'
            args['success_bool'] = True
            return render(request, 'logsys/main_page.html', args)
        else:
            args['logic_error'] = 'Something gone wrong'
            args['logic_error_bool'] = True
            return render(request, 'logsys/registration_page.html', args)
    else:
        args['form'] = form
        return render(request, 'logsys/registration_page.html', args)




