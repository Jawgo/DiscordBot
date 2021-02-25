import re
import os
import urllib
import asyncio

import requests
from bs4 import BeautifulSoup
import simplejson
import discord

import url_requester

class DiscordBot(discord.Client):
      
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello {}!'.format(message.author.display_name))
        
        
    # async def search_for_ps5(self):
    #     await self.wait_until_ready()

    #     while not self.is_closed():

    #         await asyncio.sleep(60) 
            

if __name__ == '__main__':
    print("Starting things up")
    client = DiscordBot()
    client.run(os.environ["TOKEN"])
    url_requester.check_avail()
