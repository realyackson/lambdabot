# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-20 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0011_auto_20170921_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='murphyrequest',
            name='channel_id',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]