# Generated by Django 2.0 on 2018-04-27 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0080_delete_memecontext'),
        ('facebookbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookPage',
            fields=[
                ('page_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('token', models.TextField()),
                ('image_pools', models.ManyToManyField(to='memeviewer.MemeImagePool')),
            ],
        ),
        migrations.AlterModelOptions(
            name='facebookmeem',
            options={},
        ),
        migrations.AlterField(
            model_name='facebookmeem',
            name='meme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.Meem'),
        ),
        migrations.AlterField(
            model_name='facebookmeem',
            name='post',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
        migrations.AddField(
            model_name='facebookmeem',
            name='page',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='facebookbot.FacebookPage'),
        ),
        migrations.AddIndex(
            model_name='facebookpage',
            index=models.Index(fields=['name'], name='idx_fbpage_name'),
        ),
    ]
