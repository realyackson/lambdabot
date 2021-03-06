# Generated by Django 2.0 on 2018-04-28 13:19

from django.db import migrations


def do_stuff(apps, schema_editor):
    MemeImagePool = apps.get_model('memeviewer', 'MemeImagePool')
    TwitterMeem = apps.get_model('twitterbot', 'TwitterMeem')
    TwitterPage = apps.get_model('twitterbot', 'TwitterPage')
    try:
        halflifepool = MemeImagePool.objects.get(name='halflife')
    except MemeImagePool.DoesNotExist:
        return
    mypage = None
    for m in TwitterMeem.objects.all():
        if not mypage:
            mypage = TwitterPage.objects.get_or_create(name='LambdaBot', consumer_key='', consumer_secret='', token_key='', token_secret='')[0]
            mypage.image_pools.add(halflifepool)
            mypage.save()
        m.page = mypage
        m.save()


class Migration(migrations.Migration):

    dependencies = [
        ('twitterbot', '0002_auto_20180428_1517'),
    ]

    operations = [
        migrations.RunPython(do_stuff)
    ]
