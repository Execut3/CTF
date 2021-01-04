import string

import hashlib
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import auth
from app.forms import *
from django.contrib.auth import logout
from app.models import *
import random


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    user = request.user
    shop_user = get_object_or_404(ShopUser, user=user)
    return render_to_response('index.html', locals(), RequestContext(request))


def change_alias(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    user = request.user
    shop_user = get_object_or_404(ShopUser, user=user)
    if request.method == 'POST':
        new_alias = request.POST.get('alias')

        if new_alias:
            shop_user.alias = new_alias
            shop_user.save()
    return HttpResponseRedirect('/')


def login_view(request):

    messages = {'error': '', 'success': ''}
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index')
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            # try:
            if user:
                auth.login(request, user)
                shop_user = ShopUser.objects.filter(user=user).first()
                shop_user.identifier = generate_identifier()
                shop_user.save()
                request.session['identifier'] = shop_user.identifier
                return HttpResponseRedirect('/index')
            # except:
            #     pass
        messages['error'] = 'Unable to login'
    return render_to_response('login.html', locals(), RequestContext(request))


def generate_identifier():
    return hashlib.md5(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(30))).hexdigest()


def register(request):
    messages = {'error': '', 'success': ''}
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index')
    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            if len(password) < 8 or len(username) < 8:
                messages['error'] = 'Password/Username should be at-least 8 characters'
                return render_to_response('register.html', locals(), RequestContext(request))
            email = register_form.cleaned_data['email']
            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                ShopUser.objects.get_or_create(user=user)
                messages['success'] = 'User created Successfully'
            except:
                messages['error'] = 'Error while creating user, It could be cause of user-exist, bad input & ...'
    return render_to_response('register.html', locals(), RequestContext(request))


def log_out(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect("/login")





