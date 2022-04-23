from django.contrib.auth import authenticate, login, logout

from django.shortcuts import render, redirect
from . import models, forms

from django.contrib.auth.decorators import login_required


def login_def(request):

    if request.user.is_authenticated:
        return redirect('/')

    else:
        context = {}
        if request.method == "POST":
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']

                user = authenticate(email=email, password=password)

                if user is not None:
                    login(request, user)
                    if 'next' in request.GET:
                        return redirect( request.GET.get('next') )
                    else:
                        return redirect('/')
                else:
                    context['error'] = 'Пользователь не найден'
        else:
            form = forms.LoginForm

        context['title'] = 'Авторизоваться'
        context['form'] = form
        context['button'] = 'Авторизоваться'

        return render(request, 'users/form.html', context)


def logout_def(request):
    logout(request)
    return redirect('/')


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        context = {}
        if request.method == "POST":
            form = forms.RegistrationForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                password_again = form.cleaned_data['password_again']

                if models.User.objects.filter(email=email):
                    context['error'] = 'Пользователь с таким e-mail уже существует'
                elif password != password_again:
                    context['error'] = 'Пароли не совпадают'
                else:
                    user = models.User.objects.create_user(email, password)
                    user.is_active = True
                    user.save()

                    login(request, user)

                    return redirect('/')
        else:
            form = forms.RegistrationForm

        context['title'] = 'Регистрация'
        context['form'] = form
        context['button'] = 'Зарегистрироваться'

        return render(request, 'users/form.html', context)


def index(request):
    return render(request, "users/index.html")

'''
#settings.py

AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/users/login'


path('users/', include('users.urls')),

#views.py
from django.contrib.auth.decorators import login_required

@login_required
def some_f(request):
    ...


#models.py
from django.conf import settings

class Cart(models.Model):
    some_str = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...

'''