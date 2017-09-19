# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-19 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0009_discordserveruserpermission_allow'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordServerPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(max_length=64, verbose_name='Permission')),
                ('allow', models.BooleanField(default=True, verbose_name='Allow')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbot.DiscordServer', verbose_name='Server')),
            ],
            options={
                'verbose_name': 'Server permission',
            },
        ),
        migrations.RemoveField(
            model_name='discordcommand',
            name='server_whitelist',
        ),
    ]
