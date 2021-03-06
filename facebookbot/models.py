import json
import facebook
import requests
from django.db import models, transaction
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from facebookbot.settings import FACEBOOK_API_ROOT, FACEBOOK_APP_ID, FACEBOOK_APP_SECRET
from memeviewer.models import Meem, MemeImagePool, QueuedMemeImage
from util import headers


class FacebookPage(models.Model):
    class Meta:
        indexes = [models.Index(fields=['name'], name='idx_fbpage_name')]

    page_id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=64, blank=True, default='')
    token = models.TextField(blank=True, default='')
    image_pools = models.ManyToManyField(MemeImagePool)
    enabled = models.BooleanField(default=True)

    @transaction.atomic
    def generate_meme(self):
        api = facebook.GraphAPI(self.token)
        meme = Meem.generate(self.image_pools.all(), 'fb-' + self.page_id)
        meme.make_img()
        post_status = api.put_photo(open(meme.local_path, 'rb'))
        print("post added!")
        print(post_status)
        # comment_status = api.put_comment(
        #     post_status['id'],
        #     f"template and source images: {meme.info_url}"
        # )
        # print("comment added!")
        # print(comment_status)
        return FacebookMeem.objects.create(meme=meme, page=self, post=post_status['post_id'])

    def update_token(self, temp_token):
        response = requests.get(
            f'{FACEBOOK_API_ROOT}oauth/access_token'
            f'?grant_type=fb_exchange_token'
            f'&client_id={FACEBOOK_APP_ID}'
            f'&client_secret={FACEBOOK_APP_SECRET}'
            f'&fb_exchange_token={temp_token}',
            headers=headers
        )
        long_token = json.loads(response.text)['access_token']
        response = requests.get(f'{FACEBOOK_API_ROOT}me/accounts?access_token={long_token}', headers=headers)
        for page in json.loads(response.text)['data']:
            if page['id'] == self.page_id:
                self.token = page['access_token']
                self.save()

    def __str__(self):
        return self.name or '?'


@receiver(m2m_changed, sender=FacebookPage.image_pools.through)
def pools_changed(sender, instance, **_):
    if isinstance(instance, FacebookPage):
        QueuedMemeImage.objects.filter(queue_id='fb-' + instance.page_id).delete()


class FacebookMeem(models.Model):
    meme = models.OneToOneField(Meem, on_delete=models.CASCADE)
    page = models.ForeignKey(FacebookPage, null=True, default=None, on_delete=models.SET_NULL)
    post = models.CharField(max_length=40, blank=True, default='')

    def __str__(self):
        return f"{self.meme.number} - {self.page}"
