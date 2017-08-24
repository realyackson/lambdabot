# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-24 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0005_imageincontext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageincontext',
            name='image_type',
            field=models.IntegerField(choices=[(0, 'Template'), (1, 'Source Image')]),
        ),
    ]