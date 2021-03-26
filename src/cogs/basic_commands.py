import discord
from discord.ext import commands, tasks
import asyncio

class BasicCommands(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
        


    @commands.command()
    async def hello(self, ctx):
        await ctx.channel.send('Hello {}!'.format(ctx.message.author.display_name))

    


def setup(client):
    client.add_cog(BasicCommands(client))