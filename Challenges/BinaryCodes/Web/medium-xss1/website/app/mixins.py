# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator


class MainMixin(object):
    user = None

    def check_user(self):
        return True

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):

        self.user = self.request.user

        if not self.check_user():
            raise Http404

        return super(MainMixin, self).dispatch(*args, **kwargs)


class AdminAccessOnlyMixin(MainMixin):

    def check_user(self):
        if self.user.is_superuser:
            return True
        return False


class UserAccessMixin(MainMixin):

    def check_user(self):
        if self.user.is_superuser or self.user.is_staff:
            return False
        return True

