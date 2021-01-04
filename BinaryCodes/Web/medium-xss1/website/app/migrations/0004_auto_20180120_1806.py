# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 18:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180120_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.TextField(default=b'', help_text=b'\xd8\xae\xd9\x88\xd8\xaf\xd8\xaa \xd8\xb1\xd9\x88 \xd8\xaf\xd8\xb1 \xda\xa9\xd9\x85\xd8\xaa\xd8\xb1 \xd8\xa7\xd8\xb2 \xdb\xb8\xdb\xb0 \xd8\xad\xd8\xb1\xd9\x81 \xd8\xaa\xd9\x88\xd8\xb5\xdb\x8c\xd9\x81 \xda\xa9\xd9\x86..', max_length=80),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True, verbose_name=b''),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Deselect this instead of deleting accounts.', verbose_name=b'active'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text=b'Designates whether the user can log into this admin site.', verbose_name=b'staff status'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85 \xd8\xae\xd8\xa7\xd9\x86\xd9\x88\xd8\xa7\xd8\xaf\xda\xaf\xdb\x8c'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text=b'\xd8\xa8\xd8\xa7\xdb\x8c\xd8\xaf \xd8\xb4\xd8\xa7\xd9\x85\xd9\x84 \xd8\xad\xd8\xb1\xd9\x81\xd8\x8c \xd8\xb9\xd8\xaf\xd8\xaf \xd9\x88 \xda\xa9\xd8\xa7\xd8\xb1\xd8\xa7\xda\xa9\xd8\xaa\xd8\xb1\xd9\x87\xd8\xa7\xdb\x8c @ . + - _ \xd8\xa8\xd9\x88\xd8\xaf\xd9\x87 \xd9\x88 \xd9\x86\xd8\xa8\xd8\xa7\xdb\x8c\xd8\xaf \xd8\xaa\xd8\xb9\xd8\xaf\xd8\xa7\xd8\xaf \xda\xa9\xd8\xa7\xd8\xb1\xd8\xa7\xda\xa9\xd8\xaa\xd8\xb1\xd9\x87\xd8\xa7 \xd8\xa8\xdb\x8c\xd8\xb4 \xd8\xa7\xd8\xb2 \xdb\xb3\xdb\xb0 \xd8\xa8\xd8\xa7\xd8\xb4\xd8\xaf.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile(b'^[\\w.@+-]+$'), b'\xd9\x86\xd8\xa7\xd9\x85 \xda\xa9\xd8\xa7\xd8\xb1\xd8\xa8\xd8\xb1\xdb\x8c \xd8\xb5\xd8\xad\xdb\x8c\xd8\xad \xd9\x86\xdb\x8c\xd8\xb3\xd8\xaa.', b'invalid')], verbose_name=b'\xd9\x86\xd8\xa7\xd9\x85 \xda\xa9\xd8\xa7\xd8\xb1\xd8\xa8\xd8\xb1\xdb\x8c'),
        ),
    ]
