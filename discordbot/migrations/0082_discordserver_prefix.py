# Generated by Django 2.0 on 2018-04-30 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0081_auto_20180429_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordserver',
            name='prefix',
            field=models.CharField(default='!', max_length=16),
        ),
    ]
