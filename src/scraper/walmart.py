from common import Scraper, ScrapeResult

class WalmartScrapeResult(ScrapeResult):
    def parse(self):
        alert = False

        tag = self.soup.find('button',{"data-automation":"cta-button"})
        if tag and 'add to cart' in str(tag).lower():
            alert = True

        return True

class WalmartScraper(Scraper):
    @staticmethod
    def get_domain():
        return 'walmart'
    
    @staticmethod
    def get_result_type():
        return WalmartScrapeResult