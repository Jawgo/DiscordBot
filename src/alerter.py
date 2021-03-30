import os

from discord import Webhook, RequestsWebhookAdapter, Colour, Embed


def send_alert(item):
    hook = os.environ.get("WEB_HOOK")
    webhook = Webhook.from_url(hook, adapter=RequestsWebhookAdapter())
    embedVar = Embed(title="Stock Hunter")
    if item.in_stock:
        embedVar.description = "{} **IN STOCK** at [{}]({})".format(item.item_name, item.domain, item.url)
        embedVar.colour = Colour.green()
    else:
        embedVar.description = "{} **out of stock** at [{}]({})".format(item.item_name, item.domain, item.url)
        embedVar.colour = Colour.red()
    webhook.send(embed=embedVar)
