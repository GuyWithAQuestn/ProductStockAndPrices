from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time

from selenium.webdriver.common.by import By
#import undetected_chromedriver as By
import undetected_chromedriver as uc

import DetectPlatform

from selenium.common.exceptions import TimeoutException #for urls timing out

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import undetected_chromedriver as uc
# driver = uc.Chrome()
# driver.get('https://www.example.com')

import requests

from itemWebsite import itemWebsite
from itemWebsite import itemAmazon
from itemWebsite import itemBestBuy
from itemWebsite import itemBHPhoto
from itemWebsite import itemNewEgg
from itemWebsite import itemWalmart

def get_list_of_in_stock_items(newly_added_items):

    # print("newly_added_items")
    # print(newly_added_items)

    all_new_items_available = []

    for each_item in newly_added_items:
        # print("each_item")
        # print(each_item)
        description = each_item.find('description').text
        link = each_item.find('link').text

        string_of_description_and_link = str(description) + " " + str(link)
        all_new_items_available.append(string_of_description_and_link)

    return all_new_items_available

def check_webpage_source_for_security_block(webpage_source, security_block):

    soup = BeautifulSoup(webpage_source, 'html.parser')
    if soup.findAll(text="Security Block!"):
        print("Found a security block page. We can't move on yet and will need to search it again")
    else:
        security_block = False

    return security_block

def Scrape_Website_Code(website_url):

    # If it thinks your a bot, will block the scraper. So set up headers to make it look like you're coming from Chrome (e.g. area human)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    #try to scrape the site for code and return it
    try:
        r = requests.get(website_url,headers=header)
        soup = BeautifulSoup(r.content, features='xml')

        print("Soup")
        print(soup)

        return soup



    #if something goes wrong with the scrape, return the error and throw an error
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
        return 1


def search_page_content(page_source):
    list_of_items_available = []
    list_of_items_available = page_source.findAll('item')
    return list_of_items_available

def Scrape_Website_Code(website_url):

    # If it thinks your a bot, will block the scraper. So set up headers to make it look like you're coming from Chrome (e.g. area human)
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }

    #try to scrape the site for code and return it
    try:
        r = requests.get(website_url,headers=header)
        soup = BeautifulSoup(r.content, features='xml')
        return soup
    #if something goes wrong with the scrape, return the error and throw an error
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
        return 1

def scrape_web_page_for_text(url):
    r = requests.get(url)
    page_content = BeautifulSoup(r.content, features='xml')
    return page_content

def scrape_web_page_for_source_code(driver, url):
    driver.get(url)

    # # Get the page content
    page_content = driver.page_source
    page_content_soup = BeautifulSoup(page_content, 'lxml')

    print("processing: " + url)

    if "bestbuy" in url:
        # print("bestbuy is in url")
        hard_drive = itemBestBuy(driver)
    elif "bhphotovideo" in url:
        # print("bhphotovideo is in url")
        hard_drive = itemBHPhoto(driver)
    elif "newegg" in url:
        # print("newegg is in url")
        hard_drive = itemNewEgg(driver)
    elif "walmart" in url:
        # print("walmart is in url")
        hard_drive = itemWalmart(driver)
    elif "amazon" in url:
        # print("amazon is in url")
        hard_drive = itemAmazon(driver)

    hard_drive.check_for_if_page_is_redirected(driver)

    # first, check that there is no captcha on the page!!!
    hard_drive.check_for_captcha(driver)

    #All in one method; will get an instance of the element with:
    # website_store, model_number, item_description, capacity, price, in_stock, url
    # don't really need to return anything since it'll be the properties of that instance
    hard_drive.get_item_properties(driver)

    return hard_drive, page_content_soup

def open_the_driver():
    # Generate a random user agent header using fake_useragent library
    ua = UserAgent()
    headers = {'User-Agent': ua.random}

    # Define the proxy you want to use
    proxy = 'http://p.webshare.io:9999'

    # Set up the Selenium driver with the proxy and headers
    options = Options()

#    options.add_argument('--proxy-server={}'.format(proxy))  # Comment in/out for use of proxy
    #    options.add_argument('user-agent={}'.format(headers['User-Agent']))  # Comment in/ out for change of headers
    # options.add_argument('user-agent={}'.format(headers))
    # options.add_argument('--proxy-server=proxy')
    # driver = uc.Chrome(options=options)


# Using regular chrome driver

    # options.add_argument("--no-sandbox")
    # options.add_argument("--headless") #do it without opening a web browser
    # options.add_argument("--disable-gpu")
    #

    # use chome driver
    driver = webdriver.Chrome(options=options)

    # Using undetected_chromedriver
#    driver = uc.Chrome(options=options)

    # Detect if we're running on a Pi or something else
    if (DetectPlatform.is_raspberrypi()):
        print("returned True. This is a Pi")
        ## Make sure to pass in the folder used for storing and  downloading chromedriver executable

        #use the existing chromedriver instead of downloading
        # driver = uc.Chrome(
        #     driver_executable_path="/home/pi/.local/share/undetected_chromedriver/chromedriver_copy"
        # )
        # driver.get('https://nowsecure.nl')

    else:
        print("returned False. This is not a Pi.")



    return driver


def close_the_driver(driver):
    # Close the driver
    driver.quit()
    print("driver closed")

    return 0

