import discord
import os
from pathlib import Path #require py 3.5 or later

BOT_NAME = "MyTestBot"
BOT_VERSION = "0.1-alpha"
CHANNEL_NAME = "bottest"
USE_SLASH = "Slash is da king"

def readToken():
    file = str(Path.home())+"/.discord.token"
    print("File: "+file)
    with open(file, 'r') as infile:
        data = infile.read().replace('\n', '')
        return data


class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        print("Channel: "+message.channel.name)

        #only reply to bottest
        if message.channel.name == CHANNEL_NAME:
            if message.content.startswith("/help"):
                await message.channel.send(BOT_NAME+" - "+ "\nCommands: \n/help\tDisplay help"
                                                           "\n/version\tDisplay botversion"
                                                           "\n/hostname\tDisplay bot hostname")

            if message.content.startswith("/version"):
                await message.channel.send(BOT_VERSION)

            if message.content.startswith("/hostname"):
                hostname = os.popen("hostname").read()
                await message.channel.send("Bot hostname: "+hostname)

            if message.content.startswith("!"):
                await message.channel.send(USE_SLASH)


client = BotClient()
client.run(readToken())
