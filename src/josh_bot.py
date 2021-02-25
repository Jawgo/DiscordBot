import requests
from bs4 import BeautifulSoup
import urllib
import re
import simplejson
import discord
import os

class DiscordBot(object):

    def __init__(self, token):
        self._client = discord.Client()
        self._token = token

    def start(self):
        self._client.run(self._token)

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self._client))

    async def on_message(self, message):
        if message.author == self._client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello {}!'.format(message.author))

if __name__ == '__main__':
    client = DiscordBot(os.environ["TOKEN"])
    client.start()


# print("Thrusters Activated")
# tsc_url = "https://www.tsc.ca/pages/productdetails?nav=R:643762"
# tsc_url_test = "https://www.tsc.ca/pages/productdetails?nav=R:646265&source=igodigital"

# response = requests.get(tsc_url)

# <div id="soldoutContainer" class="soldout-container-itemlevel hidden-xs">
#                   <span id="lblSoldOut" class="soldOut soldOutProduct">SOLD OUT</span>
#                </div>


# soup = BeautifulSoup(response.text, 'html.parser')
# a = soup.find('span', {"id":"lblSoldOut"})
# print(a)

# response2 = requests.get(tsc_url_test)
# soup2 = BeautifulSoup(response2.text, 'html.parser')
# b = soup2.find('span', {"id":"lblSoldOut"})
# print(b)

