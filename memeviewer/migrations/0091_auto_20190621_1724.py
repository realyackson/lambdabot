# Generated by Django 2.2.2 on 2019-06-21 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0090_auto_20180504_2357'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='memesourceimage',
            name='idx_srcimg_usages',
        ),
        migrations.RemoveIndex(
            model_name='memetemplate',
            name='idx_template_usages',
        ),
        migrations.RemoveField(
            model_name='memesourceimage',
            name='quartile',
        ),
        migrations.RemoveField(
            model_name='memesourceimage',
            name='random_usages',
        ),
        migrations.RemoveField(
            model_name='memetemplate',
            name='quartile',
        ),
        migrations.RemoveField(
            model_name='memetemplate',
            name='random_usages',
        ),
    ]
