# Generated by Django 2.0 on 2018-03-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0059_auto_20180321_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='memecontext',
            name='recent_threshold',
            field=models.IntegerField(default=14, verbose_name='Recent threshold (days)'),
        ),
    ]