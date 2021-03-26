from src.scraper.common import Scraper, ScrapeResult

class BestBuyScrapeResult(ScrapeResult):
    def parse(self):
        alert = False

        tag = self.soup.find('span',{"class":"availabilityMessage_ig-s5 container_3LC03"})
        if tag and 'available to ship' in str(tag).lower():
            alert = True

        return alert

class BestBuyScraper(Scraper):
    @staticmethod
    def get_domain():
        return 'bestbuy'
    
    @staticmethod
    def get_result_type():
        return BestBuyScrapeResult