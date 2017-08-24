# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-24 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0003_discordmeem_facebookmeem_twittermeem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facebookmeem',
            name='url',
        ),
        migrations.RemoveField(
            model_name='twittermeem',
            name='url',
        ),
        migrations.AddField(
            model_name='facebookmeem',
            name='post',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='twittermeem',
            name='post',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]