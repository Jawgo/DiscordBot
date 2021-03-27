
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class ScrapeResult(ABC):
    
    def __init__(self, result, url):
        self.soup = BeautifulSoup(result, 'lxml')
        self.url = url
        self.alert = None
        self.content = self.soup.body.text.lower()
        self.found = False
        self.parse()

    # TODO: Actually implement this method lol    
    def has_phrase(self, phrase):
        return phrase in self.content

    @abstractmethod
    def parse(self):
        pass

class Scraper(ABC):
    def __init__(self, driver, scrape_item):
        self.driver = driver
        self.url = scrape_item.url
        self.scrape_item = scrape_item

    @staticmethod
    @abstractmethod
    def get_domain():
        pass

    @staticmethod
    @abstractmethod
    def get_result_type():
        pass

    def scrape(self):
        try:
            result = self.driver.get(self.url)
            result_type = self.get_result_type()
            this_result = result_type(result, self.url)
            return this_result

        except Exception as e:
            print(f'caught exception during request: {e}')


class ScrapeItem:
    
    def __init__(self, domain, url, file):
        self.domain = domain
        self.url = url
        self.item_name = file[:-5]
        self.in_stock = False
        self.previously_in_stock = False
    
    def update_status(self, status):
        self.previously_in_stock = self.in_stock
        self.in_stock = status

class ScrapeFactory:
    registry = dict()

    @classmethod
    def create(cls, driver, scrape_item):
        for domain, scraper_type in cls.registry.items():
            if domain in scrape_item.domain:
                return scraper_type(driver, scrape_item)
    
    @classmethod
    def register(cls, scraper_type):
        domain = scraper_type.get_domain()
        cls.registry[domain] = scraper_type
        return scraper_type