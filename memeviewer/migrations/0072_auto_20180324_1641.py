# Generated by Django 2.0 on 2018-03-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0071_auto_20180324_1528'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='memesourceimage',
            index=models.Index(fields=['friendly_name'], name='idx_srcimg_fname'),
        ),
        migrations.AddIndex(
            model_name='memesourceimage',
            index=models.Index(fields=['add_date'], name='idx_srcimg_adddate'),
        ),
        migrations.AddIndex(
            model_name='memesourceimage',
            index=models.Index(fields=['change_date'], name='idx_srcimg_chdate'),
        ),
        migrations.AddIndex(
            model_name='memesourceimage',
            index=models.Index(fields=['meme_count'], name='idx_srcimg_mcount'),
        ),
        migrations.AddIndex(
            model_name='memetemplate',
            index=models.Index(fields=['friendly_name'], name='idx_template_fname'),
        ),
        migrations.AddIndex(
            model_name='memetemplate',
            index=models.Index(fields=['add_date'], name='idx_template_adddate'),
        ),
        migrations.AddIndex(
            model_name='memetemplate',
            index=models.Index(fields=['change_date'], name='idx_template_chdate'),
        ),
        migrations.AddIndex(
            model_name='memetemplate',
            index=models.Index(fields=['meme_count'], name='idx_template_mcount'),
        ),
    ]