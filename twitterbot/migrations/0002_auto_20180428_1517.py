# Generated by Django 2.0 on 2018-04-28 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0080_delete_memecontext'),
        ('twitterbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('consumer_key', models.CharField(max_length=64)),
                ('consumer_secret', models.CharField(max_length=64)),
                ('token_key', models.CharField(max_length=64)),
                ('token_secret', models.CharField(max_length=64)),
                ('enabled', models.BooleanField(default=True)),
                ('image_pools', models.ManyToManyField(to='memeviewer.MemeImagePool')),
            ],
        ),
        migrations.AlterField(
            model_name='twittermeem',
            name='meme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.Meem'),
        ),
        migrations.AlterField(
            model_name='twittermeem',
            name='post',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='twittermeem',
            name='page',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='twitterbot.TwitterPage'),
        ),
        migrations.AddIndex(
            model_name='twitterpage',
            index=models.Index(fields=['name'], name='idx_twtp_name'),
        ),
    ]
