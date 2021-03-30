import urllib
import requests
from bs4 import BeautifulSoup
import simplejson
import re
from selenium import webdriver
import os
from time import sleep
from selenium.webdriver.chrome.service import Service
import multiprocessing as mp

tsc_url = "https://www.tsc.ca/pages/productdetails?nav=R:643762"
test_good = "https://www.tsc.ca/pages/productdetails?nav=R:646265&source=igodigital"
walmart_test = "https://www.walmart.ca/en/ip/playstation5-digital-edition/6000202198823"
walmart_in_stock = "https://www.walmart.ca/en/ip/call-of-duty-black-ops-cold-war-ps5/6000201790899"

amd_5950_bb = "https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-video-card/15084753"
bb_good = ["https://www.bestbuy.ca/en-ca/product/amd-ryzen-7-3700x-octa-core-3-6ghz-am4-desktop-processor/15331710"]

URL_LIST =  [
        "https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-video-card/15084753",
        "https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14954116",
        "https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-nvidia-geforce-rtx-3080-10gb-gddr6x-video-card/14953248",
        "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3080-ventus-3x-10gb-gddr6x-video-card/14950588",
        "https://www.bestbuy.ca/en-ca/product/msi-nvidia-geforce-rtx-3090-ventus-3x-oc-24gb-gddr6x-video-card/14966477",
        "https://www.bestbuy.ca/en-ca/product/asus-rog-strix-nvidia-geforce-rtx-3090-24gb-gddr6x-video-card/14954117",
        "https://www.bestbuy.ca/en-ca/product/asus-tuf-gaming-nvidia-geforce-rtx-3090-24gb-gddr6x-video-card/14953247",
        "https://www.bestbuy.ca/en-ca/product/evga-nvidia-geforce-rtx-3090-xc3-ultra-gaming-24gb-gddr6x-video-card/14967857"
    ]

def check_avail():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--log-level=3")
    # chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    # driver = webdriver.Chrome(executable_path="C:\\Users\\Josh\\Downloads\\chromedriver", options=chrome_options)
    # service = Service("C:\\Users\\Josh\\Downloads\\chromedriver")
    # service.start()

    try:
        processList = []
        for url in bb_good:
            p = mp.Process(target=driver_run, args=(url, chrome_options,))
            processList.append(p)
            p.start()

        processFailed = False
        for p in processList:
            p.join()
            if p.exitcode is not 0:
                processFailed = True

        for p in processList:
            if p.is_alive():
                print("NO SOMETHING IS WRONG")

        if processFailed:
            print("A process failed")
    
    except Exception as e:
        print("Exception is {}".format(e))

    
    # driver.get(amd_5950_bb)
    
    # innerHTML = driver.execute_script("return document.body.innerHTML")
    # # sleep(1)
    # soup = BeautifulSoup(innerHTML, 'lxml')
    # # print(soup)
    # # tag = soup.body.select_one('class=cta')

    # tag = soup.find('span',{"class":"availabilityMessage_ig-s5 container_3LC03"})
    # print("***DEBUG***\n")
    # print(tag)
    # print("\n***********")
    # if 'available to ship' in str(tag).lower():
    #     print('IN STOCK')
    # else:
    #     print("NOT IN STOCK")

    # driver.get(bb_good)
    # innerHTML = driver.execute_script("return document.body.innerHTML")
    # soup = BeautifulSoup(innerHTML, 'lxml')
    # tag = soup.find('span',{"class":"availabilityMessage_ig-s5 container_3LC03"})
    # print("***DEBUG***\n")
    # print(str(tag).lower())
    # print("\n***********")
    # if 'available to ship' in str(tag).lower():
    #     print('IN STOCK')
    # else:
    #     print("NOT IN STOCK")
    
    ###########TEST############
    # driver.get(amd_5950_bb)
    # content = driver.find_element_by_css_selector("p.shippingAvailability_2RMa1")
    # if 'available to ship' in str(content).lower():
    #     print('IN STOCK')
    # else:
    #     print("NOT IN STOCK")

    # driver.quit()

def driver_run(url, options):
    # with webdriver.Remote(service.service_url, desired_capabilities=options.to_capabilities()) as driver:
    try:
        with webdriver.Chrome(executable_path="C:\\Users\\Josh\\Downloads\\chromedriver", options=options) as driver:
            driver.get(str(url))
            innerHTML = driver.execute_script("return document.body.innerHTML")
            soup = BeautifulSoup(innerHTML, 'lxml')
            tag = soup.find('span',{"class":"availabilityMessage_ig-s5 container_3LC03"})
            
            # tag = driver.find_element_by_css_selector("p.shippingAvailability_2RMa1")
            if 'available to ship' in str(tag).lower():
                print('IN STOCK')
            else:
                print("NOT IN STOCK")
    except Exception as e:
        print("Exception caught {}".format(e))

if __name__ == '__main__':
    check_avail()

