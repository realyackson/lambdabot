# Generated by Django 2.0 on 2018-04-27 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0078_auto_20180428_0011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discordmeem',
            name='channel_id',
        ),
        migrations.RemoveField(
            model_name='discordmeem',
            name='discord_server',
        ),
        migrations.RemoveField(
            model_name='discordserver',
            name='context',
        ),
    ]
