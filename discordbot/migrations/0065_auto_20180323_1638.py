# Generated by Django 2.0 on 2018-03-23 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0064_auto_20180323_0235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MurphyFacePic',
        ),
        migrations.RemoveField(
            model_name='murphyrequest',
            name='server_user',
        ),
        migrations.DeleteModel(
            name='MurphyRequest',
        ),
    ]
