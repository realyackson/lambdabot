import os

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render

from lamdabotweb.settings import STATIC_URL
from memeviewer.models import Meem
from memeviewer.preview import preview_meme


def meme_info_view(request, meme_id):
    try:
        meme = Meem.objects.get(meme_id=meme_id)
        if not os.path.isfile(meme.get_local_path()):
            preview_meme(meme)
    except ObjectDoesNotExist:
        raise Http404("Invalid meme ID")

    templatebg = None
    if meme.template_link.bg_img is not None:
        templatebg = STATIC_URL + 'lambdabot/resources/templates/' + meme.template_link.bg_img

    fb_meme = meme.facebookmeem_set.first()
    twitter_meme = meme.twittermeem_set.first()

    context = {
        'meme_id': meme_id,
        'meme_url': meme.get_url(),
        'meme_info_url': meme.get_info_url(),
        'template_url': STATIC_URL + 'lambdabot/resources/templates/' + meme.template_link.name,
        'template_bg_url': templatebg,
        'source_urls':
            [STATIC_URL + 'lambdabot/resources/sourceimg/' + sourceimg for sourceimg in meme.get_sourceimgs()],
        'context': meme.context_link.name,
        'gen_date': meme.gen_date,
        'num': meme.number,
        'facebook_url': fb_meme and 'https://facebook.com/{0}'.format(fb_meme.post),
        'twitter_url': twitter_meme and 'https://twitter.com/lambdabot3883/status/{0}'.format(twitter_meme.post),
    }

    return render(request, 'memeviewer/meme_info_view.html', context)
