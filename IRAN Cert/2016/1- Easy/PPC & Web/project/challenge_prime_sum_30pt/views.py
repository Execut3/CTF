__author__ = "Execut3"
'''
Challenge_1: Web-Coding category
Score: 30/500
User should send a request to /challenge-1, find the prime number,
and then calculate sum of all primes numbers less than that
value and at last create a post request to /challenge-1 with answer
parameter set to sum value.
'''


import random
from datetime import timedelta
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from challenge_prime_sum_30pt.models import *
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
                session = SessionChallenge_prime_sum.objects.get(user=request.user)
                prime_number = session.prime_number
                result_number = solve_challenge(prime_number)
                expiration_date = session.expiration_date

                if expiration_date > timezone.now():
                    if int(answer) == result_number:
                        flag = Flag.objects.get(challenge='challenge_prime_sum_30pt')
                        return HttpResponse('well done, flag is '+flag.flag)
                    else:
                        return HttpResponse('Wrong answer.')
                else:
                    return HttpResponse('Too slow, You should send your result faster.')
        except:
            return HttpResponse('There was a problem in your input parameters')
    session = update_session(request)
    prime_number = session.prime_number
    delta_time = session_expiration_delta
    return render_to_response('challenges/challenge_prime_sum.html', locals(), RequestContext(request))


@login_required(login_url='/login')
def update_session(request):

    user = request.user
    prime_number = random.randint(1000, 10000)
    expiration_date = timezone.now() + timedelta(seconds=session_expiration_delta)
    try:
        session = SessionChallenge_prime_sum.objects.get(user=user)
        session.prime_number = prime_number
        session.expiration_date = expiration_date
        session.save()
    except:
        session = SessionChallenge_prime_sum.objects.create(user=user, prime_number=prime_number,
                                                   expiration_date=expiration_date)
        session.save()
    return session


def solve_challenge(prime_number):
    prime_list = [2]
    number = 2
    while number < prime_number:
        number += 1
        is_prime = True
        for n in range(2, number/2):
            if number % n == 0:
                is_prime = False
                continue
        if is_prime:
            prime_list.append(number)
    return sum(prime_list)