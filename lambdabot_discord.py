import os
import asyncio
import requests
import shlex
import django
import discord
import re
from importlib import import_module
import time

from discordbot.permissions import PERM_MURPHYBOT, PERM_CLEVERBOT

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lamdabotweb.settings")
django.setup()

from lamdabotweb.settings import BASE_DIR, DISCORD_TOKEN
from discordbot.cleverbot import cb_talk
from discordbot.murphybot import start_murphy, is_murphy_active
from discordbot.util import log, get_server_and_member, get_attachment, discord_send, save_attachment, headers, CMD_ERR, \
    CMD_ERR_SYNTAX
from discordbot.models import ProcessedMessage, MurphyRequest

log("")
log("##############################")
log("#  LambdaBot 3883 - Discord  #")
log("##############################")
log("")

client = discord.Client(max_messages=10000)

COMMANDS = {}
COMMAND_ALIASES = {}
for file in os.listdir(os.path.join(BASE_DIR, 'discordbot', 'commands')):
    if file.startswith('__') or not file.endswith('.py'):
        continue
    md = import_module('discordbot.commands.' + os.path.splitext(file)[0])
    COMMANDS.update(md.COMMANDS)
    COMMAND_ALIASES.update(md.COMMAND_ALIASES)


# noinspection PyShadowingNames
async def _cmd_help(client, server, member, message, **_):
    await discord_send(client.send_typing, message.channel)

    helpstr = "{0} available commands:".format(message.author.mention)

    for cmd_name, cmd_data in COMMANDS.items():
        if cmd_data.get('permission') and not member.check_permission(cmd_data['permission']):
            continue

        helpstr += "\n`{0}{1}".format(server.prefix, cmd_name)

        if cmd_data.get('usage'):
            helpstr += " {}`".format(cmd_data['usage'])
        else:
            helpstr += "`"

        if cmd_data.get('help'):
            helpstr += " - {0}".format(cmd_data['help'])

    for cmd_data in server.get_commands():
        helpstr += "\n`{0}{1}`".format(server.prefix, cmd_data.cmd)

    await discord_send(client.send_message, message.channel, helpstr)

COMMANDS['help'] = {
    'function': _cmd_help,
}


@client.event
async def process_message(message):
    msg = message.content.strip()

    server, member = get_server_and_member(message)

    if re.search("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", msg) is not None:
        await asyncio.sleep(2)

    if server is None or ProcessedMessage.was_id_processed(message.id) or message.author.id == client.user.id:
        return

    att, dl_embed_url = get_attachment(message)

    if att is not None:
        if dl_embed_url is None:
            requests.get(att['proxy_url'], headers=headers)
        ProcessedMessage.process_id(message.id)

    if client.user in message.mentions:

        if msg.startswith(client.user.mention):
            msg = msg.replace(client.user.mention, "", 1).strip()
        elif msg.endswith(client.user.mention):
            msg = msg.rsplit(client.user.mention, 1)[0].strip()
        else:
            return

        log("{0}, {1}: {2}".format(server.context, message.author.name, msg))
        ProcessedMessage.process_id(message.id)

        if msg == "" and att is None:
            msg = "!help"

        answered = False

        if member.check_permission(PERM_MURPHYBOT) and is_murphy_active():
            answered = True

            if dl_embed_url is not None:
                msg = msg.replace(dl_embed_url, "", 1).strip()

            if msg.lower().startswith("what if i ") or (msg == "" and att is not None):
                face_pic = save_attachment(att['proxy_url'] if dl_embed_url is None else dl_embed_url)\
                    if att is not None else ''
                if msg == "" and att is not None:
                    MurphyRequest.ask(server_user=member, channel_id=message.channel.id, face_pic=face_pic)
                elif msg != "":
                    MurphyRequest.ask(question=msg, server_user=member, channel_id=message.channel.id, face_pic=face_pic)

            elif msg.lower().startswith("what if "):
                MurphyRequest.ask(question=msg, server_user=member, channel_id=message.channel.id)

            else:
                answered = False

        if not answered and member.check_permission(PERM_CLEVERBOT):
            await cb_talk(client, message.channel, member, msg)

        return

    if not msg.startswith(server.prefix):
        return

    try:
        splitcmd = shlex.split(msg[len(server.prefix):])
    except ValueError:
        splitcmd = msg[len(server.prefix):].split(' ')

    if len(splitcmd) == 0:
        return

    cmd = server.get_cmd(splitcmd[0])

    if cmd is not None:
        ProcessedMessage.process_id(message.id)
        await discord_send(client.send_typing, message.channel)
        await discord_send(client.send_message, message.channel, cmd.message)
        return

    cmd = COMMANDS.get(COMMAND_ALIASES.get(splitcmd[0]) or splitcmd[0])

    if cmd is None or cmd.get('permission') and not member.check_permission(cmd['permission']):
        return

    ProcessedMessage.process_id(message.id)

    cmd_fun = cmd.get('function')
    if cmd_fun is not None:
        result = await cmd_fun(
            server=server,
            member=member,
            message=message,
            args=splitcmd,
            argstr=msg[(len(server.prefix) + len(splitcmd[0])):].strip(),
            attachment=att,
            dl_embed_url=dl_embed_url,
            client=client,
        )
        if result == CMD_ERR:
            await discord_send(client.send_typing, message.channel)
            await discord_send(
                client.send_message,
                message.channel,
                "{0} error :cry:".format(message.author.mention),
            )
        elif result == CMD_ERR_SYNTAX:
            await discord_send(client.send_typing, message.channel)
            await discord_send(
                client.send_message,
                message.channel,
                "{} usage: `{}{} {}`".format(message.author.mention, server.prefix, splitcmd[0], cmd.get('usage', ''))
            )


@client.event
async def on_message(message):
    await process_message(message)


@client.event
async def on_message_edit(old_message, message):
    await process_message(message)


@client.event
async def on_message_delete(message):
    pass


@client.event
async def on_ready():
    log('Logged in as', client.user.name, client.user.id)
    await client.change_presence(game=discord.Game(name='lambdabot.morchkovalski.com'))

start_murphy(client)

while True:
    client.run(DISCORD_TOKEN)
    time.sleep(5)