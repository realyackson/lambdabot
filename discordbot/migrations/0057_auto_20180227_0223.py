# Generated by Django 2.0 on 2018-02-27 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0056_auto_20180226_0015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discordserver',
            options={'verbose_name': 'Discord server'},
        ),
        migrations.AlterModelOptions(
            name='discorduser',
            options={'verbose_name': 'Discord user'},
        ),
    ]
