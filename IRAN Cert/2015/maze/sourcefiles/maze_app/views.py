# from _mysql import IntegrityError
from datetime import datetime,timedelta
from math import floor
import re,string,random
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response
from django.utils import timezone
from maze_app.models import *
from maze_app.forms import *
from django.template import RequestContext

global SessionIntervalTime
SessionExpirationTime = 60                      # Expiration Interval of each session

global ChallengeSession
ChallengeSession = 'session_id'

global pages_list
pages_list = [
    {'name':'XSS','content':'''
        Hackers are constantly experimenting with a wide repertoire of hacking techniques to compromise websites and web applications and make off
        with a treasure trove of sensitive data including credit card numbers, social security numbers and even medical records.
        Cross-site Scripting (also known as XSS or CSS) is generally believed to be one of the most common application layer hacking techniques.
        In the pie-chart below, created by the Web Hacking Incident Database for 2011 (WHID) clearly shows that whilst many different attack methods exist,
        SQL injection and XSS are the most popular. To add to this, many other attack methods, such as Information Disclosures, Content Spoofing and Stolen
        Credentials could all be side-effects of an XSS attack.
    '''},
    {'name':'CSRF','content':'''
        Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which
        they're currently authenticated. CSRF attacks specifically target state-changing requests, not theft of data, since the attacker
        has no way to see the response to the forged request. With a little help of social engineering (such as sending a link via email
        or chat), an attacker may trick the users of a web application into executing actions of the attacker's choosing. If the victim
        is a normal user, a successful CSRF attack can force the user to perform state changing requests like transferring funds, changing
        their email address, and so forth. If the victim is an administrative account, CSRF can compromise the entire web application.
    '''},
    {'name':'Injection','content':'''
        Injection Attacking occurs when there are flaws in your SQL Database, SQL libraries, or even the operating system itself.
        Employees open seemingly credible files with hidden commands, or 'injections', unknowingly.
        In doing so, they've allowed hackers to gain unauthorized access to private data such as social security numbers,
        credit card number or other financial data.
    '''},
    {'name':'Remote-Code-Execution','content':'''
        A Remote Code Execution attack is a result of either server side or client side security weaknesses.
        Vulnerable components may include libraries, remote directories on a server that haven't been monitored,
        frameworks, and other software modules that run on the basis of authenticated user access. Applications
        that use these components are always under attack through things like scripts, malware, and small command
        lines that extract information.
        The following vulnerable components were downloaded 22 million times in 2011:
        Apache CXF Authentication Bypass (http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3451)
        By failing to provide an identity token, attackers could invoke any web service with full permission.
    '''},
    {'name':'Clickjacking','content':'''
        Clickjacking, also called a UI Redress Attack, is when a hacker uses multiple opaque layers to trick
        a user into clicking the top layer without them knowing.
        Thus the attacker is 'hijacking' clicks that are not meant for the actual page, but for a page where
        the attacker wants you to be.
        For example, using a carefully crafted combination of stylesheets, iframes, and text boxes, a user can be led
        to believe they are typing in the password for their bank account, but are actually typing into an invisible
        frame controlled by the attacker.
    '''},
    {'name':'DNS-Poisoning','content':'''
        DNS Cache Poisoning involves old cache data that you might think you no longer have on your computer,
        but is actually 'toxic'.
        Also known as DNS Spoofing, hackers can identify vulnerabilities in a domain name system, which allows
         them to divert traffic from legit servers to a fake website and/or server.
        This form of attack can spread and replicate itself from one DNS server to another DNS, 'poisoning'
         everything in it's path.
        In fact, in 2010, a DNS poisoning attack completely compromised the Great Firewall of China (GFC)
         temporarily and censored certain content in the United States until the problem was fixed.
    '''},
    {'name':'Social-Engineering','content':'''
        A social engineering attack is not technically a 'hack'.
        It happens when you divulge private information in good faith, such as a credit card number,
        through common online interactions such as email, chat, social media sites, or virtually any website.
        The problem, of course, is that you're not getting into what you think you're getting into.
        A classic example of a social engineering attack is the 'Microsoft tech support' scam.
    '''},
    {'name':'D-DOS','content':'''
        DDoS, or Distributed Denial of Services, is where a server or a machine's services are made unavailable
        to its users.
        And when the system is offline, the hacker proceeds to either compromise the entire website or a specific
        function of a website to their own advantage.
        It's kind of like having your car stolen when you really need to get somewhere fast.
        The usual agenda of a DDoS campaign is to temporarily interrupt or completely take down a successfully
        running system.
    '''}
]

global flag_sequence
# flag_sequence = [0,1,2,0,3,6,4,7,5]                 # Index 0 is not counted...
flag_sequence = [[0,1,2,8,3,6,4,7,5],
                 [0,3,5,2,4,8,6,1,7],
                 [0,5,6,4,2,7,8,3,1],
                 [0,7,8,6,1,4,2,5,3],
                 [0,1,3,6,7,4,2,5,8],
                 [0,8,3,6,2,4,7,5,1],
                 [0,1,3,7,6,4,2,5,8],
                 [0,3,1,6,7,2,4,8,5],
                 [0,1,4,6,7,3,2,5,8],
                 ]
# flag_sequence = [0,1,1,1,1,1,1,1,1]                 # Index 0 is not counted...

def MainPage(request,page):
    try:
        sqli = ''
        if re.findall('\'|\"',page):
            if not re.findall('\'  --+|\'--+|\'--;|\' --;|\' --|\'--',page):
                sqli = 'You have an error in your SQL syntax; check the manual that corresponds to your MySQL server' \
                                    'version for the right syntax to use near %s at line 1'%page
        elif page:
            if request.method=='GET' and request.META['HTTP_USER_AGENT']=='S3CR37':
                try:
                    current_session = request.COOKIES[ChallengeSession]
                    if current_session:
                        session_obj = Sessions.objects.get(session_key=current_session)
                        if session_obj.expiration_date > timezone.now():
                            try:
                                for i in pages_list:
                                    if i['name'] == page:
                                        page_index = pages_list.index(i)
                                if page_index is None:
                                    raise Http404
                                random_id = session_obj.random_id
                                if session_obj.sequence_id == 0 or session_obj.sequence_id > 8:
                                    return HttpResponse('Even MAZE has an Entry...')
                                if flag_sequence[random_id][int(session_obj.sequence_id)] == page_index+1:
                                    if session_obj.sequence_id == 8:
                                        return HttpResponse('Even MAZE has an END!, Flag is: I_Kn3W_Y0U_W!ll_M4K3_It_Th!5_F4R')
                                    session_obj.sequence_id += 1
                                    session_obj.save()
                                    return HttpResponse('Keep Going...')
                                else:
                                    session_obj.sequence_id = 1
                                    session_obj.save()
                                    return HttpResponse('You\'re LOST! Try again...')
                            except:
                                raise Http404
                        else:
                            Sessions.objects.get(session_key=current_session).delete()
                            return HttpResponse('Do you know even sessions EXPIRE!!!')
                except:
                    return HttpResponse('Who are you?')
            else:
                for i in pages_list:
                    if i['name']==page:
                        name = page
                        content = i['content']
        else:
            HttpResponseRedirect('/main')
    except:
        pass
    return render_to_response('../../maze/templates/main.html', locals(), RequestContext(request))

def Main(request):
    if request.method=='GET' and request.META['HTTP_USER_AGENT']=='S3CR37':
        try:
            current_session = request.COOKIES[ChallengeSession]
            if current_session:
                session_obj = Sessions.objects.get(session_key=current_session)
                if session_obj.expiration_date > timezone.now():
                    session_obj.sequence_id = 1
                    session_obj.save()
                    return HttpResponse('Welcome to the MAZE... Now let\' ROLL!!!')
                else:
                    Sessions.objects.get(session_key=current_session).delete()
                    return HttpResponse('Do you know even sessions EXPIRE!!!')
        except:
            return HttpResponse('Who Are You???')
    if request.method == 'POST':
        try:
            current_session = request.COOKIES[ChallengeSession]
            if current_session:
                session_obj = Sessions.objects.get(session_key=current_session)
                if session_obj.expiration_date > timezone.now():
                    return HttpResponse("Now I know you buddy. how you doin! i really don't know where the door is, but i know only S3CR37 agents can GET to maze!")
                else:
                    Sessions.objects.get(session_key=current_session).delete()
                    return HttpResponse('If you had come earlier I Could tell you where is the door! but now I can just say SORRY!!!khkhkh')
        except:
            return HttpResponse("I know the door for MAZE... But i'm not gonna tell you. Who are you that asking me that question!!!")
    pages = pages_list
    return render_to_response('../../maze/templates/main.html',locals(),RequestContext(request))

def Subscribe(request):
    try:
        subscribe = ''
        if request.method=="POST":
            username = request.POST['username']
            subscribe = request.POST['subscribe']
    except:
        pass
    return render_to_response('../../maze/templates/subscribe.html', locals(), RequestContext(request))

def Session(request):
    message = ''
    my_session = ''
    form = SessionForm()
    if request.method=="POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if re.match(r"^[a-zA-Z0-9]{1,}$", username)!=None:
                for i in Sessions.objects.filter(username=username):
                    if i.expiration_date < timezone.now():
                        i.delete()
                # Situation that user tries to get a new session_key
                # First if it already set a session in this request
                try:
                    if request.COOKIES[ChallengeSession]:
                        try:
                            current_session = request.COOKIES[ChallengeSession]
                            if Sessions.objects.get(session_key=current_session):
                                Sessions.objects.get(session_key=current_session).delete()
                        except Exception as e:
                            pass
                except:
                    pass    # If comes to this, means that session is not set by user
                # Second if no session is set by the user
                new_session = create_session(100, string.ascii_lowercase) + '_' + username
                # Create session here...
                try:
                    expiration_date = timezone.now() + timedelta(seconds=SessionExpirationTime)
                    flag_sequence_len = len(flag_sequence)
                    random_id = int(floor(random.random()*flag_sequence_len%flag_sequence_len))
                    Sessions.objects.create(username=username, session_key=new_session, expiration_date=expiration_date, random_id=random_id).save()
                    message = 'Tadahhhh... You got a session now!'
                    my_session = new_session
                except:
                    message = 'Username not unique... Sorry the Session is in use'
    return render_to_response('../../maze/templates/session.html', locals(), RequestContext(request))
floor
def create_session(size,chars):
    return ''.join(random.choice(chars) for _ in range(size))


# if re.match(r"^[a-zA-Z0-9._]+\@[a-zA-Z0-9._]+\.[a-zA-Z]{3,}$", email)!=None:

def Admin(request):
    if request.method == "POST":
        return HttpResponse('Not Available!!!')
    return render_to_response('../../maze/templates/admin.html',locals(),RequestContext(request))
