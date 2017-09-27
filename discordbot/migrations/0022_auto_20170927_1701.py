# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-27 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0021_murphyfacepic_last_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Permission')),
            ],
            options={
                'verbose_name': 'Permission',
            },
        ),
        migrations.AlterField(
            model_name='discordserverpermission',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbot.DiscordPermission', verbose_name='Permission'),
        ),
        migrations.AlterField(
            model_name='discordserveruserpermission',
            name='permission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbot.DiscordPermission', verbose_name='Permission'),
        ),
    ]
