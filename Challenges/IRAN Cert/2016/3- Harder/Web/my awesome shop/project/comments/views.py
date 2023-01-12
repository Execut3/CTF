from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from app.models import ShopUser
from comments.models import Comment


def create_new(request):
    if request.method == 'POST':
        user = request.user
        get_object_or_404(ShopUser, user=user)
        content = request.POST.get('content', '')
        print content
        if content:
            try:
                Comment.objects.create(user=user, content=content)
            except:
                comment = Comment.objects.get(user=user, content=content)
                comment.active = False
                comment.save()
    return HttpResponseRedirect(reverse('view_comments'))


def view(request):
    user = request.user
    get_object_or_404(ShopUser, user=user)
    comments = Comment.objects.filter(user=user)
    return render_to_response('comments/view.html', locals(), RequestContext(request))


def flush(request):
    user = request.user
    get_object_or_404(ShopUser, user=user)
    Comment.objects.filter(user=user).delete()
    return render_to_response('comments/view.html', locals(), RequestContext(request))