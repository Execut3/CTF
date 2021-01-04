# -*- coding: utf-8 -*-
from csp.decorators import csp_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import UpdateView

from app.forms import *
from .mixins import *

User = get_user_model()


@csp_exempt
def login_view(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    if not request.method == 'POST':
        login_form = LoginForm()
        return render(request, 'app/login.html', locals())

    messages = {'success': '', 'error': ''}
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            messages['error'] = 'کاربر در سیستم ثبت نشده است.'
    else:
        print(login_form.errors)
        messages['error'] = 'لطفا اطلاعات فرم را به درستی تکمیل نمایید.'
    print(messages)
    return render(request, 'app/login.html', locals())


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register_view(request, **kwargs):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    if not request.method == 'POST':
        register_form = RegisterForm()
        return render(request, 'app/register.html', locals())

    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
        username = register_form.cleaned_data['username']
        first_name = register_form.cleaned_data['first_name']
        last_name = register_form.cleaned_data['last_name']
        email = register_form.cleaned_data['email']
        password = register_form.cleaned_data['password']

        is_registered_user = User.objects.filter(Q(username=username) | Q(email=email)).exists()
        if is_registered_user:
            error = 'کاربری با این مشخصات قبلا در سامانه ثبت‌نام نموده است.'
        else:
            user = User.objects.create(username=username, email=email)
            print(user)
            user.set_password(password)
            user.is_active = True
            user.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        error = 'لطفا اطلاعات درخواستی را به درستی وارد نمایید.'

    return render(request, 'app/register.html', locals())


@login_required(login_url='login')
def index(request):
    return render(request, 'app/index.html', locals())


@login_required(login_url='login')
def flag_view(request):
    print('flag')
    if not request.user.is_superuser:
        return render(request, 'app/flag.html', locals())
    flag = 'flag_5dd1abc0e13c94838c466d6f32f1f4fd'
    return render(request, 'app/flag.html', locals())


def profile(request, **kwargs):
    if not request.user.is_authenticated:
        raise Http404
    pk = kwargs.get('pk')
    if request.user.is_superuser:
        user = User.objects.filter(pk=pk).first()
    else:
        user = request.user
    return render(request, 'app/profile.html', locals())


class ProfileEditView(MainMixin, UpdateView):
    template_name = 'app/profile_edit.html'
    form_class = BasicInfoUserForm
    form_name = 'user_form'
    model = User

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def get_context_data(self, **kwargs):
        context = super(ProfileEditView, self).get_context_data(**kwargs)
        context.update({
            'user_form': BasicInfoUserForm(),
        })
        return context

    def get_object(self, queryset=None):
        return self.user


profile_edit = ProfileEditView.as_view()


@login_required(login_url='login')
def change_avatar(request):
    avatar = request.FILES.get('avatar')
    form = BasicInfoUserForm(instance=request.user)
    error = ''

    if not avatar:
        error = 'فایل نمی‌تواند خالی باشد.'
        return render(request, 'app/profile_edit.html', locals())

    avatar_name = avatar.name
    avatar_content_type = avatar_name.split('.')[-1]
    if not avatar_content_type in ['png', 'jpg', 'jpeg', 'gif']:
        error = 'باید یکی از فرمت‌های png، gif، jpg و یا jpeg باشد.'
        return render(request, 'app/profile_edit.html', locals())

    request.user.avatar = avatar
    request.user.save()
    return HttpResponseRedirect(reverse('profile', kwargs={'pk': request.user.pk}))
