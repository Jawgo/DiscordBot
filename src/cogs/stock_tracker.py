import discord
from discord.ext import commands, tasks
import asyncio

from src.driver import Driver
from src.scraper.bestbuy import BestBuyScraper

class StockTracker(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        self.driver = Driver()
        # Hardcoding a link for now, will incorporate something to check multiple links
        self.url = "https://www.bestbuy.ca/en-ca/product/amd-ryzen-9-5950x-16-core-3-4ghz-am4-desktop-processor/15331716"
        self.bb = BestBuyScraper(self.driver, self.url)
        self.in_stock = False

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ready to track things")


    @commands.command()
    async def list_trackers(self, ctx):
        await ctx.send("Ryzen 9 5950x")

    @tasks.loop(seconds=60.0)
    async def check_sites(self):
        scrape_result = self.bb.scrape()
        result = scrape_result.parse()
        if result and not self.in_stock:
            channel = self.client.get_channel(797324359051116556)
            self.in_stock = True
            await channel.send("In STOCK {}".format(scrape_result.url))
        elif not result and self.in_stock:
            await channel.send("Out of Stock {}".format(scrape_result.url))

    


def setup(client):
    client.add_cog(StockTracker(client))