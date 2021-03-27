import discord
from discord.ext import commands, tasks
import asyncio
# import datetime

from src.hunter import Hunter


class StockTracker(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.hunter = None

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready to track things")

    #TODO: Finish with the this method. can do some cooler things with it
    #Then do we need something to stop the scheduler? Maybe each time we
    #sched something we keep track of it?
    @commands.command()
    async def list_trackers(self, ctx):
        await self.client.wait_until_ready()
        if self.hunter:
            tmp_scrapers = self.hunter.get_scrape_list()
            title = "Hunter Tracking Status"
            des = "Inventory Status of All items being hunted"
            embedVar = discord.Embed(title=title, description=des, colour=discord.Colour.orange())
            for scraper in tmp_scrapers:
                item = scraper.scrape_item
                name = "{} at {}".format(item.item.name,scraper.get_domain())
                if item.in_stock:
                    msg = "**IN STOCK**"
                else:
                    msg = "out of stock"
                embedVar.add_field(name=name, value=msg, inline=False)
                # embedVar.timestamp = datetime.now()
            await ctx.channel.send(embed=embedVar)
        else:
            await ctx.channel.send("The hunter is asleep")

    @commands.command()
    async def start_tracking(self, ctx):
        await self.client.wait_until_ready()
        if not self.hunter:
            embedVar = discord.Embed(title="Stock Hunter", description="Starting to hunt for inventory", color=discord.Colour.green())
            await ctx.channel.send(embed=embedVar)
            self.hunter = Hunter(self.alert)
            self.hunter.run()
        else:
            embedVar = discord.Embed(title="Stock Hunter", description="Already Running Dawg", color=discord.Colour.blue())
            # embedVar.timestamp = datetime.now()
            await ctx.channel.send(embed=embedVar)

        

    @commands.command()
    async def stop_tracking(self, ctx):
        await self.client.wait_until_ready()
        if self.hunter:
            del self.hunter
            embedVar = discord.Embed(title="Stock Hunter", description="Stoping the hunt for inventory", color=discord.Colour.red())
        else:
            embedVar = discord.Embed(title="Stock Hunter", description="Hunting has not been activated", color=discord.Colour.blue())
        # embedVar.timestamp = datetime.now()
        await ctx.channel.send(embed=embedVar)
        

    async def alert(self, item):
        await self.client.wait_until_ready()
        channel = self.client.get_channel(797324359051116556)
        embedVar = discord.Embed(title="Stock Hunter")
        if item.in_stock:
            embedVar.description = "{} **IN STOCK** at {}".format(item.item_name, item.url)
            embedVar.colour = discord.Colour.green()
        else:
            embedVar.description = "{} **out of stock** at {}".format(item.item_name, item.url)
            embedVar.colour = discord.Colour.red()
        # embedVar.timestamp = datetime.now()
        await channel.send(embed=embedVar)
    


def setup(client):
    client.add_cog(StockTracker(client))