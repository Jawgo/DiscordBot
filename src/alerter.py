import os

from discord import Webhook, RequestsWebhookAdapter, Colour, Embed

class Alerter():
    
    def __init__(self):
        print("Alerter Started")
        self.hook = os.environ["WEB_HOOK"]
        self.webhook = Webhook.from_url(self.hook, adapter=RequestsWebhookAdapter())


    def send_alert(self, item):
        embedVar = Embed(title="Stock Hunter")
        if item.in_stock:
            embedVar.description = "{} **IN STOCK** at [{}]({})".format(item.item_name, item.domain, item.url)
            embedVar.colour = Colour.green()
        else:
            embedVar.description = "{} **out of stock** at [{}]({})".format(item.item_name, item.domain, item.url)
            embedVar.colour = Colour.red()
        self.webhook.send(embed=embedVar)
