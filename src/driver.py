import os
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class Driver():

    def __init__(self):
        self.driver_path = os.environ.get("CHROMEDRIVER_PATH")
        # self.driver_path = "C:\\Users\\Josh\\Downloads\\chromedriver"
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--headless")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-gpu")
        # self.options.add_argument("--disable-features=NetworkService")
        self.options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        self.options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36")
        self.setup_service()

    def setup_service(self):
        self.service = Service(self.driver_path)
        self.service.start()

    def get(self, url):
        # with webdriver.(executable_path=self.driver_path, chrome_options=self.options) as driver:
        with webdriver.Remote(self.service.service_url, desired_capabilities=self.options.to_capabilities()) as driver:
            driver.get(str(url))
            innerHTML = driver.execute_script("return document.body.innerHTML")
            driver.quit()
            return innerHTML

if __name__ == '__main__':
    driver = Driver()
    