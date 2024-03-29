import json
import os
import sched
from pathlib import Path, PurePosixPath
import random
import multiprocessing as mp

from src.driver import Driver
from src.scraper.common import ScrapeItem
from src.scraper import init_scrapers
from src.alerter import send_alert

REFRESH_INTERVAL = 2
random.seed()

class Hunter():

    def __init__(self):
        self.config_path = Path("./src/configs/")
        self.scrape_items = []
        self.files = self.load_files()
        self.driver = Driver()
        self.scrapers = None
        self.setup()
        self.scrapers = init_scrapers(self.driver, self.scrape_items)

        # self.scheduler = sched.scheduler()
        # for s in self.scrapers:
    #         self.schedule(s)
        
    # def run(self):
    #     self.scheduler.run(blocking=True)

    # def schedule(self, scraper):
    #     time_delta = REFRESH_INTERVAL
    #     time_delta *= random.randint(100,120) / 100.0

    #     if self.scheduler.queue:
    #         # This is taking the time scheduled and adding a delta to
    #         # it to create randomness 
    #         t = self.scheduler.queue[-1].time + time_delta
    #         self.scheduler.enterabs(t, 1, Hunter.hunt, (self, scraper))
    #     else:
    #         self.scheduler.enter(time_delta, 1, Hunter.hunt, (self, scraper))

    # New way to search for stock, uses a process for each scraper and finds all at once, if something is found, will
    # send an alert through web hook. Could make this endless, and just get the bot to stop, or make it a background task
    def run(self):
        try:
            processList = []
            for scraper in self.scrapers:
                p = mp.Process(target=self.hunt, args=(scraper, 200, ))
                processList.append(p)
                p.start()

            processFailed = False
            for p in processList:
                p.join()
                if p.exitcode is not 0:
                    processFailed = True

            for p in processList:
                if p.is_alive():
                    print("Process was found to still be alive!")

            if processFailed:
                print("A process failed, but no exception was raised??")
    
        except Exception as e:
            print("Exception is {}".format(e))


    def process_result(self, scraper, result):
        print("Processing result for {}".format(scraper.scrape_item.item_name))
        item = scraper.scrape_item
        print("BEFORE Item Prev: {}, Item Now: {} for {} result is {}".format(item.previously_in_stock, item.in_stock, item.item_name, result.found))
        item.update_status(result.found)
        print("AFTER Item Prev: {}, Item Now: {} for {} result is {}".format(item.previously_in_stock, item.in_stock, item.item_name, result.found))
        if item.previously_in_stock ^ item.in_stock:
            send_alert(item)
            
    def load_files(self):
        files = []
        for filename in os.listdir(self.config_path):
            if filename.endswith('.json'):
                files.append(filename)
        return files


    def get_json(self, filename):
        with open(self.config_path / filename) as json_file:
            data = json.load(json_file)
            json_file.close()
            return data

    def setup(self):
        for file in self.files:
            data = self.get_json(file)
            for domain in data:
                for url in data[domain]:
                    self.scrape_items.append(ScrapeItem(domain, url, file))
    
    def hunt(self, scraper, num):
        i =  num
        while i > 0:
            print("Hunting")
            result = scraper.scrape()
            item = scraper.scrape_item.item_name
            url = scraper.scrape_item.url
            if result is None:
                print("Something went wrong with {} for {}".format(url, item))
            else:
                self.process_result(scraper, result)
            i -= 1
        

    def get_scrape_list(self):
        return self.scrapers

if __name__ == "__main__":
    h = Hunter()
    h.run()
                

                


        

        
        



# in theory we have a bunch of json files, that give urls for specific Scrapers,
# like bestbuy, walmart, etc. Scraper factory creates a pairing of all our 
# scrapers with domain names
