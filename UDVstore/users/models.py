from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    phone = models.CharField(_('phone'), max_length=30, blank=True)
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    position = models.CharField(_('position'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)

    is_active = models.BooleanField(_('is_active'), default=False)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Возвращает сокращенное имя пользователя.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)