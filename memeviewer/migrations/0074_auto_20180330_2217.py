# Generated by Django 2.0 on 2018-03-30 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0073_auto_20180330_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memesourceimageincontext',
            name='all_usages',
        ),
        migrations.RemoveField(
            model_name='memetemplateincontext',
            name='all_usages',
        ),
    ]
