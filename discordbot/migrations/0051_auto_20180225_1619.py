# Generated by Django 2.0 on 2018-02-25 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0050_auto_20180225_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discordcommandalias',
            name='cmd',
        ),
        migrations.RemoveField(
            model_name='discordcommand',
            name='help',
        ),
        migrations.RemoveField(
            model_name='discordcommand',
            name='help_params',
        ),
        migrations.RemoveField(
            model_name='discordcommand',
            name='permission',
        ),
        migrations.DeleteModel(
            name='DiscordCommandAlias',
        ),
    ]
