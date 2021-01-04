# -*- coding: utf-8 -*-
from collections import OrderedDict

from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label='نام کاربری')
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label='پسورد')
    # captcha = CaptchaField(label='عبارت امنیتی')


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label='نام کاربری')
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label='پسورد')
    email = forms.EmailField(widget=forms.TextInput(), label='آدرس ایمیل',
                             help_text='eg: example@example.com')
    first_name = forms.CharField(widget=forms.TextInput(), label='نام')
    last_name = forms.CharField(widget=forms.TextInput(), label='نام خانوادگی')
    # captcha = CaptchaField(label='عبارت امنیتی')


class AvatarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AvatarForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = {'avatar'}


class BasicInfoUserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BasicInfoUserForm, self).__init__(*args, **kwargs)

        original_fields = self.fields
        new_order = OrderedDict()
        for key in ['first_name', 'last_name', 'email', 'description']:
            new_order[key] = original_fields[key]
        self.fields = new_order

    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'description', }


