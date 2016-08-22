# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='oauth_secret',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='oauth_token',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
