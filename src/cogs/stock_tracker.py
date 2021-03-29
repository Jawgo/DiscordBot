import discord
from discord.ext import commands, tasks
import asyncio
# import datetime
from threading import Thread

from src.hunter import Hunter


class StockTracker(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.hunter = None
        self.thread = None

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
                name = "{} at {}".format(item.item_name,scraper.get_domain())
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
            # self.alert.start()
            self.hunter = Hunter(self)
            self.thread = Thread(target=self.hunter.run())
            self.thread.start()

            # self.hunter.run()
        else:
            embedVar = discord.Embed(title="Stock Hunter", description="Already Running Dawg", color=discord.Colour.blue())
            # embedVar.timestamp = datetime.now()
            await ctx.channel.send(embed=embedVar)

        

    @commands.command()
    async def stop_tracking(self, ctx):
        await self.client.wait_until_ready()
        if self.hunter:
            del self.hunter
            del self.thread
            # self.alert.stop()
            embedVar = discord.Embed(title="Stock Hunter", description="Stoping the hunt for inventory", color=discord.Colour.red())
        else:
            embedVar = discord.Embed(title="Stock Hunter", description="Hunting has not been activated", color=discord.Colour.blue())
        # embedVar.timestamp = datetime.now()
        await ctx.channel.send(embed=embedVar)
        

    # @tasks.loop(seconds = 60)
    # async def alert(self):

    # TODO: What i am thinking is that we have a loop that will check for alerts
    #       One option is that it is a task loop that will run, pass in a list that will
    #       be populated with alerts and then based on the status, send an alert?
    #       within the hunter, create a pool and run each one on a sep thread and join results


    # TODO: Another option is that we spin off the process like stated above, but pass in the client and do an alert when
        #   something is in stock? Try this first? wouldnt have to change much?
    #
    #
    #

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