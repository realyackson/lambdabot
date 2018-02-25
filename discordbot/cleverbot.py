from cleverwrap import CleverWrap
from json.decoder import JSONDecodeError
from discordbot.util import DelayedTask, discord_send, log
from lamdabotweb.settings import CLEVERBOT_TOKEN

cb_conversations = {}


async def cb_talk(client, channel, user, message, nodelay=False):
    sender_id = user.user.user_id
    if cb_conversations.get(sender_id) is None:
        log("creating session for {}".format(user), tag="cleverbot")
        cb_conversations[sender_id] = CleverWrap(CLEVERBOT_TOKEN)

    response = "There's an error here <@257499042039332866>"
    success = False
    retries = 5
    while not success and retries > 0:
        try:
            response = cb_conversations[sender_id].say(message)
            success = True
        except JSONDecodeError:
            log("cleverbot error! recreating session for {}".format(user), tag="cleverbot")
            cb_conversations[sender_id] = CleverWrap(CLEVERBOT_TOKEN)
            retries -= 1

    log("response: {}".format(response), tag="cleverbot")
    delay = 0 if nodelay else 0.2 + min(0.04 * len(message), 4)
    if delay > 0:
        DelayedTask(delay, discord_send, (client.send_typing, channel)).run()
        delay += min(0.17 * len(response), 4)
    DelayedTask(delay, discord_send, (client.send_message, channel, "<@{0}> {1}".format(sender_id, response))).run()