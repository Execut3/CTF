# -*- coding: utf-8 -*-
from django.conf import settings


ADMIN_USERNAME = getattr(settings, 'ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = getattr(settings, 'ADMIN_PASSWORD', 'RRLgahscjbvARWVF')
BASE_URL = getattr(settings, 'BASE_URL', 'http://127.0.0.1:8000')
