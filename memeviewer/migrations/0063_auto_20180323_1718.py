# Generated by Django 2.0 on 2018-03-23 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memeviewer', '0062_memecontext_meme_count'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageincontext',
            options={},
        ),
        migrations.AlterField(
            model_name='imageincontext',
            name='context_link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='memeviewer.MemeContext'),
        ),
        migrations.AlterField(
            model_name='imageincontext',
            name='image_name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='imageincontext',
            name='image_type',
            field=models.IntegerField(),
        ),
    ]
