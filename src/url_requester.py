import urllib
import requests
from bs4 import BeautifulSoup
import simplejson
import re
from selenium import webdriver
import os

tsc_url = "https://www.tsc.ca/pages/productdetails?nav=R:643762"
test_good = "https://www.tsc.ca/pages/productdetails?nav=R:646265&source=igodigital"
walmart_test = "https://www.walmart.ca/en/ip/playstation5-digital-edition/6000202198823"
walmart_in_stock = "https://www.walmart.ca/en/ip/call-of-duty-black-ops-cold-war-ps5/6000201790899"
def check_avail():

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(walmart_in_stock)
    print(driver.page_source)
    driver.quit()

    # captcha = False
    # user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    # headers = {'user-agent': user_agent, 'referrer': 'https://google.com'}
    # url = walmart_in_stock
    # response = requests.get(url, headers=headers)
    # soup = BeautifulSoup(response.text, 'html.parser')
    # a = soup.find('span', {"id":"lblSoldOut"})
    # return a
    # a = soup.find('p',{"class":"css-k008qs e9yijxp1"})
    # print(soup)
    # a = soup.find_all(string="Out of stock")

    # print(strings)
    
    
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
    # test, test1 = check_avail()
    # print(test)
    # print(test1)
  



# print("Thrusters Activated")

# tsc_url_test = "https://www.tsc.ca/pages/productdetails?nav=R:646265&source=igodigital"

# response = requests.get(tsc_url)

# <div id="soldoutContainer" class="soldout-container-itemlevel hidden-xs">
#                   <span id="lblSoldOut" class="soldOut soldOutProduct">SOLD OUT</span>
#                </div>


# soup = BeautifulSoup(response.text, 'html.parser')
# a = soup.find('span', {"id":"lblSoldOut"})
# print(a)

# response2 = requests.get(tsc_url_test)
# soup2 = BeautifulSoup(response2.text, 'html.parser')
# b = soup2.find('span', {"id":"lblSoldOut"})
# print(b)

