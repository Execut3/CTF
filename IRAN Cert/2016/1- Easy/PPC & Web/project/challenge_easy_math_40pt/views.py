__author__ = "Execut3"
'''
Challenge_0: Web-Coding category
Score: 50/500
User should send a request to /index, find the random number,
and then create a post request to /challenge-0 with answer
parameter set to sum value.
'''


import random
from datetime import timedelta
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from challenge_easy_math_50pt.models import *
from django.utils import timezone
from app.models import Flag


session_expiration_delta = 10000


def index(request):
    global session_expiration_delta
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    if request.method == 'POST':
        try:
            answer = request.POST['answer']
            if answer:
                session = SessionChallenge_easy_math.objects.get(user=request.user)
                result = session.result

                expiration_date = session.expiration_date
                if expiration_date > timezone.now():
                    if int(answer) == result:
                        flag = Flag.objects.get(challenge='challenge_easy_math_50pt')
                        return HttpResponse('well done, flag is '+flag.flag)
                    else:
                        return HttpResponse('Wrong answer.')
                else:
                    return HttpResponse('Too slow, You should send your result faster.')
        except:
            return HttpResponse('There was a problem in your input parameters')
    session = update_session(request)
    num1 = session.num1
    num2 = session.num2
    operator = session.operator
    delta_time = session_expiration_delta
    return render_to_response('challenges/challenge_easy_math.html', locals(), RequestContext(request))


def update_session(request):
    operator_list = ['+', '-', '*', '%']
    user = request.user
    num1 = random.randint(1000, 10000)
    num2 = random.randint(1000, 10000)
    operator = operator_list[random.randint(0, len(operator_list)-1)]
    equation = '%i%s%i'%(num1, operator, num2)
    result = eval(equation)
    print result
    expiration_date = timezone.now() + timedelta(seconds=session_expiration_delta)

    try:
        session = SessionChallenge_easy_math.objects.get(user=user)
        session.num1 = num1
        session.num2 = num2
        session.operator = operator
        session.result = result
        session.expiration_date = expiration_date
        session.save()
    except:
        session = SessionChallenge_easy_math.objects.create(user=user, num1=num1, num2=num2, operator=operator,
                                                            result=result, expiration_date=expiration_date)
        session.save()
    return session