# -*- coding: utf-8 -*-
import re

import PIL.Image as Image
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
from django.core import validators
from django.db import models
from django.utils import timezone

from django.utils.translation import ugettext as _

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def avatar_images_upload_address(instance, filename):
    upload_dir = "avatar/%s" % filename
    return upload_dir


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=False,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField('نام کاربری', max_length=30, unique=True,
                                help_text='باید شامل حرف، عدد و کاراکترهای @ . + - _ بوده و نباید تعداد کاراکترها بیش از ۳۰ باشد.',
                                validators=[
                                    validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                                              'نام کاربری صحیح نیست.',
                                                              'invalid')
                                ])
    first_name = models.CharField('نام', max_length=30, blank=True, null=True)
    last_name = models.CharField('نام خانوادگی', max_length=30, blank=True, null=True)
    email = models.EmailField('', max_length=255, null=True, blank=True)

    description = models.TextField(max_length=80, default='', help_text='خودت رو در کمتر از ۸۰ حرف توصیف کن..')

    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=False,
                                    help_text=_(
                                        'Designates whether this user should be treated as active. '
                                        'Deselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    receive_newsletter = models.BooleanField(_('receive newsletter'), default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    avatar = models.ImageField(upload_to=avatar_images_upload_address, blank=True, null=True, max_length=1500)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        if not self.first_name and not self.last_name:
            full_name = self.username
        else:
            full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        # if not self.pk:
        #     if self.avatar:
        #         avatar = Image.open(self.avatar.path)
        #         avatar = avatar.resize((200, 200), Image.ANTIALIAS)
        #         avatar.save(self.avatar.path)

    def __unicode__(self):
        return self.username

