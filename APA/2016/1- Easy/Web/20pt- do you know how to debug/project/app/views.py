from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from app.models import flag


def calculator(num1, num2, operator):
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return False


def index(request):
    if request.method == 'POST':
        num1 = request.POST['num1']
        num2 = request.POST['num2']
        operator = request.POST['operator']
        if num1 and num2 and operator:
            result = calculator(num1, num2, operator)

        try:
            debug = request.POST['debug_me']
        except:
            debug = False


        if debug:
            flag = find_flag(request)
            if flag:
                return HttpResponse('well done, flag is '+flag)

    return render_to_response('index.html', locals(), RequestContext(request))


def find_flag(request):
    int(request.POST['debug_me'])
    my_flag = flag.objects.all()[0]
    get_flag = request.POST['get_flag']
    if get_flag == 'yes':
        return my_flag.name