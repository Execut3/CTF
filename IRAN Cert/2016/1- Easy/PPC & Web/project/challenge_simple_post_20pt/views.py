__author__ = "Execut3"
'''
Challenge_0: Web-Coding category
Score: 10/500
User should send a request to /index, find the random number,
and then create a post request to /challenge-0 with answer
parameter set to sum value.
'''


import random
from datetime import timedelta
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from challenge_simple_post_10pt.models import *
from django.utils import timezone
from app.models import Flag
from django.contrib.auth.decorators import login_required


session_expiration_delta = 10000


@login_required(login_url='/login')
def index(request):
    global session_expiration_delta
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        try:
            answer = request.POST['answer']
            if answer:
                session = SessionChallenge_simple_post.objects.get(user=request.user)
                random_number = session.random_number
                expiration_date = session.expiration_date

                if expiration_date > timezone.now():
                    if int(answer) == random_number:
                        flag = Flag.objects.get(challenge='challenge_simple_post_10pt')
                        return HttpResponse('well done, flag is '+flag.flag)
                    else:
                        return HttpResponse('Wrong answer.')
                else:
                    return HttpResponse('Too slow, You should send your result faster.')
        except:
            return HttpResponse('There was a problem in your input parameters')
    session = update_session(request)
    random_number = session.random_number
    delta_time = session_expiration_delta
    return render_to_response('challenges/challenge_simple_post.html', locals(), RequestContext(request))


@login_required(login_url='/login')
def update_session(request):

    user = request.user
    random_number = random.randint(1000, 10000)
    expiration_date = timezone.now() + timedelta(seconds=session_expiration_delta)
    try:
        session = SessionChallenge_simple_post.objects.get(user=user)
        session.random_number = random_number
        session.expiration_date = expiration_date
        session.save()
    except:
        session = SessionChallenge_simple_post.objects.create(user=user, random_number=random_number,
                                                   expiration_date=expiration_date)
        session.save()
    return session