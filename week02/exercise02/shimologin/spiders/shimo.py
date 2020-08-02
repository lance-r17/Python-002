import scrapy
from scrapy.exceptions import NotConfigured
from selenium import webdriver
import time

from scrapy.utils.project import get_project_settings

class ShimoSpider(scrapy.Spider):
    name = 'shimo'
    allowed_domains = ['shimo.im']
    start_urls = ['https://shimo.im/login?from=home']

    def start_requests(self):
        browser = webdriver.Chrome()
        # 需要安装chrome driver, 和浏览器版本保持一致
        # http://chromedriver.storage.googleapis.com/index.html

        browser.get('https://shimo.im/login?from=home')

        settings = get_project_settings()

        if not settings.get('SHIMO_USERNAME'):
            raise NotConfigured('Shimo user name is not configured yet')

        if not settings.get('SHIMO_PASSWORD'):
            raise NotConfigured('Shimo password is not configured yet')

        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys(settings.get('SHIMO_USERNAME'))
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys(settings.get('SHIMO_PASSWORD'))
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

        # cookies = browser.get_cookies()
        # print(cookies)
        time.sleep(3)

        yield scrapy.Request(url='https://shimo.im/dashboard', callback=self.parse)

    def parse(self, response):
        # print(response)
        pass
