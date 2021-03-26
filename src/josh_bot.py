import os
import asyncio
import discord
from discord.ext import commands

# class DiscordBot(discord.Client):
class DiscordBot(commands.Bot):

    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self))
        await self.change_presence(status=discord.Status.online, activity=discord.Game('Hunt for Things'))

    @commands.command()
    async def hello(self, ctx):
        await ctx.channel.send('Hello {}!'.format(ctx.message.author.display_name))

    
            

if __name__ == '__main__':
    print("Starting things up")
    intents = discord.Intents.default()
    client = DiscordBot(command_prefix="!", intents=intents)
    client.load_extension('cogs.stock_tracker')
    client.run(os.environ["TOKEN"])
