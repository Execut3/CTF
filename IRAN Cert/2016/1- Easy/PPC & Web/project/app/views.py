__author__ = "Execut3"
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import auth
from app.forms import *
from django.contrib.auth import logout
from app.models import *


def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    return render_to_response('index.html', locals(), RequestContext(request))


def login(request):
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
            try:
                if user:
                    auth.login(request, user)
                    return HttpResponseRedirect('/index')
            except:
                pass
        messages['error'] = 'Unable to login'
    return render_to_response('login.html', locals(), RequestContext(request))


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
            email = register_form.cleaned_data['email']
            try:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                messages['success'] = 'User created Successfully'
            except:
                messages['error'] = 'Error while creating user, It could be cause of user-exist, bad input & ...'
    return render_to_response('register.html', locals(), RequestContext(request))


def log_out(request):
    if request.user.is_authenticated():
        logout(request)
    return HttpResponseRedirect("/login")





