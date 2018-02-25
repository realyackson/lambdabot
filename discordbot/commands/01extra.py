import json
import random
import textwrap
import re
import requests

from bs4 import BeautifulSoup
from discord import Embed
from discordbot.util import discord_send, log_exc, headers, CMD_ERR_SYNTAX, CMD_ERR

COMMANDS = {}
COMMAND_ALIASES = {}


async def _cmd_led(client, message, args, argstr, **_):
    await discord_send(client.send_typing, message.channel)

    if len(args) == 1:
        return CMD_ERR_SYNTAX

    response = requests.post('http://wigflip.com/signbot/', data={
        'T': argstr,
        'S': 'L',
    }, headers=headers)

    soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
    img = soup.select_one('#output img')
    if img is not None:
        await discord_send(
            client.send_message,
            message.channel,
            "{0} {1}".format(message.author.mention, img['src']),
        )
    else:
        return CMD_ERR

COMMANDS['led'] = {
    'function': _cmd_led,
    'help': 'generate an LED sign',
    'usage': '(text)'
}


async def _cmd_mario(client, message, args, **_):
    await discord_send(client.send_typing, message.channel)

    if len(args) < 3 or len(args) > 4:
        return CMD_ERR_SYNTAX

    if len(args) == 4:
        name = args[1]
        title = args[2]
        msgtext = args[3]
    else:
        name = None
        title = args[1]
        msgtext = args[2]

    response = requests.post('http://wigflip.com/thankyoumario/', data={
        'name': name,
        'title': title,
        'lines': msgtext,
        'double': 'y',
    }, headers=headers)

    soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
    img = soup.select_one('#output img')
    if img is not None:
        await discord_send(
            client.send_message,
            message.channel,
            "{0} {1}".format(message.author.mention, img['src']),
        )
    else:
        return CMD_ERR

COMMANDS['mario'] = {
    'function': _cmd_mario,
    'help': 'generate a mario thing',
    'usage': '[name] (first line) (message)'
}


async def _cmd_noviews(client, message, **_):
    await discord_send(client.send_typing, message.channel)

    attempt = 0
    videourl = None
    while videourl is None and attempt < 5:
        try:
            response = requests.get('http://www.petittube.com', headers=headers)
            soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")
            videourl = re.search('\/(\w+)\?', soup.select_one('iframe')['src']).groups()[0]
        except Exception as e:
            attempt += 1

    if videourl is None:
        return CMD_ERR
    else:
        await discord_send(
            client.send_message,
            message.channel,
            "{0} https://youtu.be/{1}".format(message.author.mention, videourl),
        )

COMMANDS['noviews'] = {
    'function': _cmd_noviews,
    'help': 'show random youtube video with no views',
}


async def _cmd_wiki(client, message, args, argstr, **_):
    await discord_send(client.send_typing, message.channel)

    wiki_url = 'http://combineoverwiki.net'
    article = None
    was_random = False

    if len(args) == 1:
        try:
            was_random = True
            response = requests.get(
                '{0}/api.php?action=query&generator=random&grnnamespace=0&grnlimit=1&prop=info&inprop=url&format=json'.format(wiki_url),
                headers=headers,
            )
            article_data = json.loads(response.content.decode('utf-8'))
            article = next(iter(article_data['query']['pages'].values()))

        except Exception as exc:
            log_exc(exc)

    else:
        try:
            query = argstr
            response = requests.get(
                '{0}/api.php?action=query&generator=search&gsrsearch={1}&gsrlimit=1&prop=info&inprop=url&format=json'.format(wiki_url, query),
                headers=headers,
            )
            article_data = json.loads(response.content.decode('utf-8'))
            if article_data.get('query') is not None:
                article = next(iter(article_data['query']['pages'].values()))
        except Exception as exc:
            log_exc(exc)

    proceed = False
    soup = None

    while not proceed:
        if article is None:
            await discord_send(
                client.send_message,
                message.channel,
                "{0} article not found :cry:".format(message.author.mention)
            )
            return

        response = requests.get(article['fullurl'], headers=headers)
        soup = BeautifulSoup(response.content.decode('utf-8'), "html5lib")

        heading = soup.select_one('#firstHeading')
        if not was_random or heading is None or not heading.getText().lower().endswith('(disambiguation)'):
            proceed = True
        else:
            page_links = soup.select('#mw-content-text > ul:nth-of-type(1) > li')
            random_page = random.choice([li.select_one('a:nth-of-type(1)').getText() for li in page_links])
            if random_page is None:
                article = None
            else:
                response = requests.get(
                    '{0}/api.php?action=query&generator=search&gsrsearch={1}&gsrlimit=1&prop=info&inprop=url&format=json'.format(
                        wiki_url, random_page),
                    headers=headers,
                )
                article_data = json.loads(response.content.decode('utf-8'))
                if article_data.get('query') is not None:
                    article = next(iter(article_data['query']['pages'].values()))

    pic_tag = soup.select_one('td.infoboximage > a > img')
    if pic_tag is None:
        pic_tag = soup.select_one('img.thumbimage')

    desc_tag = soup.select_one('div#mw-content-text > p:nth-of-type(2)')
    desc = textwrap.shorten(desc_tag.getText(), width=250) if desc_tag is not None else None

    embed = Embed(
        title=article['title'],
        url=article['fullurl'],
        color=0xF7923A,
        description=desc,
    )
    embed.set_footer(
        text="Combine Overwiki",
        icon_url="http://combineoverwiki.net/images/1/12/HLPverse.png".format(wiki_url)
    )

    if pic_tag is not None:
        embed.set_thumbnail(url="{0}{1}".format(wiki_url, pic_tag['src']))
        # embed.set_image(url="{0}{1}".format(wiki_url, pic_tag['src']))

    await discord_send(
        client.send_message,
        message.channel,
        "{0} {1}".format(message.author.mention, article['fullurl']),
        embed=embed,
    )

COMMANDS['wiki'] = {
    'function': _cmd_wiki,
    'help': 'search the half-life overwiki',
    'usage': '[query]'
}