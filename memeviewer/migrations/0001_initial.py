# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-24 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meem',
            fields=[
                ('number', models.IntegerField()),
                ('meme_id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('template', models.CharField(max_length=64)),
                ('sourceimgs', models.TextField()),
                ('context', models.CharField(max_length=32)),
                ('gen_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
