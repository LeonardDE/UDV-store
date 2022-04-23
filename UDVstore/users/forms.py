from turtle import position
from django import forms
from django.contrib.auth.models import User

from . import models


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email",)
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")


class ForgotPassword(forms.Form):
    email = forms.EmailField(label="Email",)


class ChangePassword(forms.Form):
    password_1 = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
    password_2 = forms.CharField(widget=forms.PasswordInput(), label="Еще раз пароль")


class RegistrationForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль")
    password_again = forms.CharField(widget=forms.PasswordInput(), label="Еще раз пароль")

    name = forms.CharField(max_length=150, label="Имя",)
    position = forms.CharField(max_length=150, label="Должность",)
    phone = forms.CharField(max_length=150, label="Номер",)
    