# Generated by Django 2.0 on 2017-12-27 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0038_remove_discordserveruser_no_edits_log'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='discordserveruserpermission',
            unique_together=set(),
        ),
    ]
