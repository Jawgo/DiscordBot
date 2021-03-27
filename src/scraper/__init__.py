import src.scraper.bestbuy

#Once new scrapers are established, import them here

from src.scraper.common import ScrapeFactory

def init_scrapers(driver, scrape_items):
    return [ScrapeFactory.create(driver, scrape_item) for scrape_item in scrape_items]