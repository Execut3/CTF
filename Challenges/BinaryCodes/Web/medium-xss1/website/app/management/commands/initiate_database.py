# -*- coding: utf-8 -*-

from django.core.management import BaseCommand

from app.app_settings import ADMIN_PASSWORD, ADMIN_USERNAME
from app.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        User.objects.create_superuser(username=ADMIN_USERNAME, password=ADMIN_PASSWORD, email='admin@admin.admin')
