from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm


def main_page(request):
    args = {}
    return render(request, 'logsys/main_page.html')


def user_login(request):
    args = {}
    form = LoginForm()
    if request.POST:
        new_form = LoginForm(request.POST)
        if new_form.is_valid():
            username = new_form.cleaned_data['username']
            password = new_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                args['user'] = user
                args['success'] = 'Вы успешно вошли'
                return render(request, 'logsys/main_page.html', args)
            else:
                args['form'] = form
                args['logic_error'] = 'There are no such users'
        else:
            args['form'] = form
            args['logic_error'] = 'Something worng'
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
    form = RegistrationForm()
    if request.POST:
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password1 = user_form.cleaned_data['password1']
            password2 = user_form.cleaned_data['password2']
            email = user_form.cleaned_data['email']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            if password1 == password2:
                user = User.objects.create_user(username=username, email=email, password=password2, first_name=first_name, last_name=last_name)
                user.save()
                user = authenticate(username=username, password=password2)
                if user is not None:
                    login(request, user)
                    args['user'] = user
                    args['success'] = 'Вы успешно зарегестрировались'
            return render(request, 'logsys/main_page.html', args)
        else:
            args['form'] = form
            args['logic_error'] = 'Something gone wrong'
    else:
        args['form'] = form
    return render(request, 'logsys/registration_page.html', args)




