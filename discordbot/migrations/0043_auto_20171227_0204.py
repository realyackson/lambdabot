# Generated by Django 2.0 on 2017-12-27 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discordbot', '0042_auto_20171227_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscordServerPerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow', models.BooleanField(default=True, verbose_name='Allow')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbot.DiscordPerm', verbose_name='Permission')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbot.DiscordServer', verbose_name='Server')),
            ],
            options={
                'verbose_name': 'Server permission',
            },
        ),
        migrations.CreateModel(
            name='DiscordServerUserPerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow', models.BooleanField(default=True, verbose_name='Allow')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbot.DiscordPerm', verbose_name='Permission')),
                ('server_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discordbot.DiscordServerUser', verbose_name='Server user')),
            ],
            options={
                'verbose_name': 'Server user permission',
            },
        ),
        migrations.RemoveField(
            model_name='discordserverpermission',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='discordserverpermission',
            name='server',
        ),
        migrations.AlterUniqueTogether(
            name='discordserveruserpermission',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='discordserveruserpermission',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='discordserveruserpermission',
            name='server_user',
        ),
        migrations.DeleteModel(
            name='DiscordServerPermission',
        ),
        migrations.DeleteModel(
            name='DiscordServerUserPermission',
        ),
        migrations.AlterUniqueTogether(
            name='discordserveruserperm',
            unique_together={('server_user', 'permission')},
        ),
    ]
