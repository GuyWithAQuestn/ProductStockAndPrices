from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

from selenium.webdriver.common.by import By

import requests


# Classes
class itemWebsite:
    def __init__(self, capacity, page_source):
        self.capacity = capacity
        self.page_source = page_source
        self.in_stock = False
        self.price = "."
        self.website = ".."

    def check_if_item_in_stock(self,page_source):
        print(page_source)
        try:
            # page_source.find_element(By.XPATH, '//button[text()="Add to Cart"]')
            page_source.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page")
            print("Item is for NOT sale currently")
            # print(e)

        return self.in_stock

    def get_price_of_item(self,page_source):
        # price = ""
        try:
            what_I_found = page_source.find_element(By.XPATH, '//div[@class="price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        except Exception as e:
            print("Class is not available on the page Price")
            # print(e)

        return self.price

class itemBestBuy(itemWebsite):
    def __init__(self, capacity, pagesource):
        super().__init__(capacity,pagesource)
        self.website = "Best Buy"
    def get_price_of_item(self,page_source):
        price = ""
        try:
            what_I_found = page_source.find_element(By.XPATH, '//div[@class="priceView-hero-price priceView-customer-price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        except Exception as e:
            print("Class is not available on the page Price")
            # print(e)
        return self.price

class itemBHPhoto(itemWebsite):
    def __init__(self, capacity, pagesource):
        super().__init__(capacity,pagesource)
        self.website = "B&H Photo"
    def check_if_item_in_stock(self,page_source):
        print(page_source)
        try:
            #BH Photo sometimes has Add to Cart buttons, but also has "Out of Stock" text on those pages, too.
            #Not truly in stock
            page_source.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page")
            print("Item is for NOT sale currently")
#            print(e)

        #Even if Add to Cart is present, sometimes "Temporarily Out of Stock" comes up
        print("trying temp out of stock text")
        try:
            page_source.find_element(By.XPATH, '//span[contains(text(),"Temporarily Out of Stock")]')
            self.in_stock = False
            print("Item is for NOT sale currently")
        except Exception as e:
            print("there is NOT a Temporarily Out of Stock on the page, so it must be in stock")

        return self.in_stock

    def get_price_of_item(self,page_source):
        try:
            what_I_found = page_source.find_element(By.XPATH, '//div[@class="price_L0iytPTSvv"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        except Exception as e:
            print("Class is not available on the page Price")
#            print(e)
        return self.price

class itemNewEgg(itemWebsite):
    def __init__(self, capacity, pagesource):
        super().__init__(capacity,pagesource)
        self.website = "NewEgg"
    def check_if_item_in_stock(self,page_source):
        print(page_source)
        try:
            # page_source.find_element(By.XPATH, '//button[text()="Add to Cart"]')
            page_source.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page")
            print("Item is for NOT sale currently")
            # print(e)

        return self.in_stock
    def get_price_of_item(self,page_source):
        try:
            what_I_found = page_source.find_element(By.XPATH, '//div[@class="product-offer"]')
        except Exception as e:
            print("Class is not available on the page Price")
            # print(e)

        self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)

        return self.price

class itemWalmart:
    def __init__(self, capacity, pagesource):
        super().__init__(capacity,pagesource)
        self.website = "Walmart"
    def __init__(self, capacity, page_source):
        self.capacity = capacity
        self.page_source = page_source
        self.in_stock = False
        self.price = ""

    def check_if_item_in_stock(self,page_source):

        print(page_source)
        try:
            # page_source.find_element(By.XPATH, '//button[text()="Add to cart"]')
            page_source.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
            #https://www.geeksforgeeks.org/python-selenium-find-button-by-text/
            #Note: It is recommended to use normalize-space() method because it trim the left and right side spaces. It is possible that there can be spaces present at the start or at the end of the target text.

            print("reached here")
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page")
            print("Item is for NOT sale currently")
            # print(e)

        return self.in_stock

    def get_price_of_item(self,page_source):

        try:
            what_I_found = page_source.find_element(By.XPATH, '//span[@itemprop="price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)

        except Exception as e:
            print("Class is not available on the page Price")
            # print(e)

        return self.price


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



    # # For each of the items in the XML code...
    # for each_item in all_items:
    #     #            print ("in for loop")
    #     title = each_item.find('title').text
    #     description = each_item.find('description').text
    #     link = each_item.find('link').text
    #     published = each_item.find('pubDate').text
    #     single_item = {
    #         'title': title,
    #         'description': description,
    #         'link': link,
    #         'published': published
    #     }



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
        return soup
    #if something goes wrong with the scrape, return the error and throw an error
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)
        return 1


def search_page_content(page_source):
    list_of_items_available = []

#    soup_of_page_source = BeautifulSoup(page_source, 'lxml')

#    print("soup_of_page_source: ")
#    print(soup_of_page_source)

    list_of_items_available = page_source.findAll('item')

    # print("list_of_items_available: ")
    # print(list_of_items_available)


    # # For each of the items in the XML code...
    # for each_item in all_items:
    #     #            print ("in for loop")
    #     title = each_item.find('title').text
    #     description = each_item.find('description').text
    #     link = each_item.find('link').text
    #     published = each_item.find('pubDate').text
    #     single_item = {
    #         'title': title,
    #         'description': description,
    #         'link': link,
    #         'published': published
    #     }

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

#def scrape_web_page(driver, url):
def scrape_web_page_for_text(url):

    # # Navigate to the URL
    # driver.get(url)

    r = requests.get(url)
    page_content = BeautifulSoup(r.content, features='xml')

    # # Get the page content
    # page_content = driver.page_source

#    print("Here's some page_content")
#    print(page_content)

    # Print the page content
    # print(page_content)

    # Get the page content
    # page_content = driver.execute_script("return document.documentElement.outerHTML")
    # # Save the page content to a file
    # with open('/Users/bryan/Downloads/output.html', 'w', encoding='utf-8') as f:
    #     f.write(page_content)

    return page_content




def scrape_web_page_for_source_code(driver, url):
#def scrape_web_page_for_source_code(url):

    # # Navigate to the URL
    driver.get(url)

    # r = requests.get(url)
    # page_content = BeautifulSoup(r.content, features='xml')

    # # Get the page content
    page_content = driver.page_source
    page_content_soup = BeautifulSoup(page_content, 'lxml')

    # Find the button using text
#    driver.find_element_by_xpath('//button[normalize-space()="Click me!"]').click()


# ***********

    print("url")
    print(url)
    if "bestbuy" in url:
        print("bestbuy is in url")
        hard_drive = itemBestBuy('18TB', driver)
    elif "bhphotovideo" in url:
        print("bhphotovideo is in url")
        hard_drive = itemBHPhoto('18TB', driver)
    elif "newegg" in url:
        print("newegg is in url")
        hard_drive = itemNewEgg('18TB', driver)
    elif "walmart" in url:
        print("walmart is in url")
        hard_drive = itemWalmart('18TB', driver)

    stock_check = hard_drive.check_if_item_in_stock(driver)

    print("stock_check")
    print(stock_check)

    item_price = hard_drive.get_price_of_item(driver)
    print("item_price")
    print(item_price)


#     try:
#         what_I_found = driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')
#
#         print("what_I_found")
#         print(what_I_found)
#         print("Item is for sale currently")
#
#     except Exception as e:
#         print("Class is not available on the page")
#         print("Item is for NOT sale currently")
#
#     try:
# #        what_I_found = driver.find_element(By.XPATH, '//div[@class="priceView-hero-price priceView-customer-price"]')
#         what_I_found = driver.find_element(By.XPATH, '//div[@class="price_L0iytPTSvv"]')
#
#         print("what_I_found Price")
#         print(what_I_found)
#
#         price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#
#
#     except Exception as e:
#         print("Class is not available on the page Price")
#         price = ""
#
#     print("price :$" + price)
#     # print(price)

# ***********

    #
    # # NOTE: Had to initialize driver="" above because it would retain other webpage iterations information if not previously cleared
    # if driver.find('div', class_='priceView-hero-price priceView-customer-price'):
    #     priceSentence = driver.find('div', class_='priceView-hero-price priceView-customer-price')
    #     print("priceSentence: ")
    #     print(priceSentence)
    #     price = (re.search('\$(\d+,?\d*\.\d+)', priceSentence.text)).group(1)
    # else:
    #     price = ""
    #
    # print("price:")
    # print(price)

    # # Wait for the class to become available on the page
# try:
#     #    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='my-button']")))
#     element = WebDriverWait(driver, 10).until(
#         # EC.presence_of_element_located((By.CLASS, "power-calendar-container")))
#         # element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "ember64")))
#     #    for button in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='"+ first_time_from_list +"']"))):
#     #        button.click()
#     print("Found The Class I was Waiting For!")
#     # button.click()
# except Exception as e:
#     print("Class is not available on the page")
#     #    print(e)








#    driver.findElement(By.linkText("Add to Cart")):

    # for button in WebDriverWait(driver, 20).until(
    #     EC.visibility_of_all_elements_located((By.XPATH, "//button[text()='" + time_to_book + "']"))):
    #
    # button_list = soup_of_page_source_for_url.find_all('button', {
    #     'class': 'service-availability-select-or-call-button custom-color-bg custom-color-border-color btn btn-block btn-primary ember-view'})

#    print("Here's some page_content")
#    print(page_content)

    # Print the page content
    # print(page_content)

    # Get the page content
    # page_content = driver.execute_script("return document.documentElement.outerHTML")
    # # Save the page content to a file
    # with open('/Users/bryan/Downloads/output.html', 'w', encoding='utf-8') as f:
    #     f.write(page_content)

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
    driver = webdriver.Chrome(options=options)

    return driver


def close_the_driver(driver):
    # Close the driver
    driver.quit()
    print("driver closed")

    return 0

