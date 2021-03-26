
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup

class ScrapeResult(ABC):
    
    def __init__(self, result, url):
        self.soup = BeautifulSoup(result, 'lxml')
        self.url = url
        self.alert = None
        self.content = self.soup.body.text.lower()
        
    def has_phrase(self, phrase):
        return phrase in self.content

    @abstractmethod
    def parse(self):
        pass

class Scraper(ABC):
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

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