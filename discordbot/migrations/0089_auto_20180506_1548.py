# Generated by Django 2.0 on 2018-05-06 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0088_auto_20180504_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discordchannel',
            name='name',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='discordserver',
            name='name',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='name',
            field=models.CharField(blank=True, default='', max_length=512),
        ),
    ]