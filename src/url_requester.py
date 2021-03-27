import urllib
import requests
from bs4 import BeautifulSoup
import simplejson
import re
from selenium import webdriver
import os
from time import sleep

tsc_url = "https://www.tsc.ca/pages/productdetails?nav=R:643762"
test_good = "https://www.tsc.ca/pages/productdetails?nav=R:646265&source=igodigital"
walmart_test = "https://www.walmart.ca/en/ip/playstation5-digital-edition/6000202198823"
walmart_in_stock = "https://www.walmart.ca/en/ip/call-of-duty-black-ops-cold-war-ps5/6000201790899"

amd_5950_bb = "https://www.bestbuy.ca/en-ca/product/evga-geforce-rtx-3080-xc3-ultra-gaming-10gb-gddr6x-video-card/15084753"
bb_good = "https://www.bestbuy.ca/en-ca/product/amd-ryzen-7-3700x-octa-core-3-6ghz-am4-desktop-processor/15331710"
def check_avail():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--disable-features=NetworkService")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver = webdriver.Chrome(executable_path="C:\\Users\\Josh\\Downloads\\chromedriver", options=chrome_options)

    driver.get(amd_5950_bb)

    innerHTML = driver.execute_script("return document.body.innerHTML")
    # sleep(1)
    soup = BeautifulSoup(innerHTML, 'lxml')
    # print(soup)
    # tag = soup.body.select_one('class=cta')
    print("sleeping")
    sleep(30)
    tag = soup.find('span',{"class":"availabilityMessage_ig-s5 container_3LC03"})
    print("***DEBUG***\n")
    print(tag)
    print("\n***********")
    if 'available to ship' in str(tag).lower():
        print('IN STOCK')
    else:
        print("NOT IN STOCK")

    driver.get(bb_good)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(innerHTML, 'lxml')
    tag = soup.find('span',{"class":"availabilityMessage_ig-s5 container_3LC03"})
    print("***DEBUG***\n")
    print(str(tag).lower())
    print("\n***********")
    if 'available to ship' in str(tag).lower():
        print('IN STOCK')
    else:
        print("NOT IN STOCK")
    driver.quit()
    
    
     ####################
     #UNCOMMENT LATER##
     ###################
    # soup = BeautifulSoup(response.text, 'lxml')
    # content = soup.body.text.lower()
    # print(soup)
    # soup.body.select_one('section.prod-ProductCTA.primaryProductCTA-marker button')
    # alert_subject = ''
    # alert_content = ''

    # # detect captcha
    # tag = soup.body.find('div', id='px-captcha')
    # if tag:
    #     captcha = True
    #     return

    # # get name of product
    # tag = soup.body.select_one('h1.prod-ProductTitle.prod-productTitle-buyBox.font-bold')
    # print(tag)
    # if tag:
    #     alert_content += tag.text.strip() + '\n'
    # else:
    #     print(f'missing title: {url}')

    # # get listed price
    # tag = soup.body.select_one('section.prod-PriceSection div.prod-PriceHero span.price-group')
    # print(f'This was found for price: {tag}')
    # price_str = tag
    # if price_str:
    #     alert_subject = f'In Stock for {price_str}'
    # else:
    #     print(f'missing price: {url}')

    # # check for add to cart button
    # tag = soup.body.select_one('section.prod-ProductCTA.primaryProductCTA-marker button')
    # print(tag)
    # if tag and 'add to cart' in str(tag).lower():
    #     alert_subject = alert_subject
    #     alert_content = f'{alert_content.strip()}\n{url}'
    # else:
    #     alert_subject = 'Not in Stock'


    # return alert_subject, alert_content

if __name__ == '__main__':
    check_avail()

