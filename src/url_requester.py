import urllib
import requests
from bs4 import BeautifulSoup
import simplejson

tsc_url = "https://www.tsc.ca/pages/productdetails?nav=R:643762"
def check_avail():
    response = requests.get(tcs_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    a = soup.find('span', {"id":"lblSoldOut"})

if __name__ == '__main__':
    


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

