import discord
from discord.ext import commands, tasks
import asyncio

class BasicCommands(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):

    # embeded message example, play around with it    
    # @client.event
    # async def on_message(message):
    # if message.content.startswith('!hello'):
    #     embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    #     embedVar.add_field(name="Field1", value="hi", inline=False)
    #     embedVar.add_field(name="Field2", value="hi2", inline=False)
    #     await message.channel.send(embed=embedVar)

    @commands.command()
    async def hello(self, ctx):
        await ctx.channel.send('Hello {}!'.format(ctx.message.author.display_name))

    


def setup(client):
    client.add_cog(BasicCommands(client))