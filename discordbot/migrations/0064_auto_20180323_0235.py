# Generated by Django 2.0 on 2018-03-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0063_auto_20180323_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordserver',
            name='meme_count',
            field=models.IntegerField(default=0, verbose_name='Generated memes'),
        ),
        migrations.AddField(
            model_name='discordserver',
            name='submission_count',
            field=models.IntegerField(default=0, verbose_name='Submitted source images'),
        ),
    ]
