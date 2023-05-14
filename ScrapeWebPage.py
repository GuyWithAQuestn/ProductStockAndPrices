from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time

from selenium.webdriver.common.by import By
#import undetected_chromedriver as By
import undetected_chromedriver as uc

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


# # Classes
# class itemWebsite:
#     # def __init__(self, driver, expected_capacity):
#     #     self.expected_capacity = expected_capacity
#     def __init__(self, driver):
#         # self.expected_capacity = expected_capacity
#         self.capacity = '.'
#         self.page_source = driver
#         self.in_stock = False
#         self.price = ".."
#         self.website = "..."
#         self.successfully_found_element = True
#
#     def check_for_if_page_is_redirected(self, driver):
#         #pages like BHPhoto will refer to another product when something isn't in stock.
#         #leave this blank and just pass through in most circumstances
#         pass
#         return 0
#
#     def check_for_captcha(self,driver):
#         pass
#         return 0
#     def check_if_item_in_stock(self,driver):
#         print(driver)
#         try:
#             driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')
#             #driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
#             self.in_stock = True
#         except Exception as e:
#             print("Class is not available on the page; no Add to Cart button")
#             print("Item is for NOT sale currently")
#             # print(e)
#             self.successfully_found_element = False
#
#         return self.in_stock
#
#     def get_price_of_item(self,driver):
#         # price = ""
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//div[@class="price"]')
#             self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#         except Exception as e:
#             print("Class is not available on the page Price")
#             # print(e)
#             self.successfully_found_element = False
#
#         return self.price
#
#     def get_capactity_of_item(self, driver):
#         price = ""
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//h1[@class="heading-5 v-fw-regular"]')
#             self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             self.capacity = self.expected_capacity
#             # print(e)
#
#         # strip out the TB from the 12TB so that it's just a string of an integer
#         self.capacity = (re.search(r'\d+', what_I_found.text)).group()
#
#         return self.capacity
#
# class itemBestBuy(itemWebsite):
#     # def __init__(self, driver,expected_capacity):
#     #     super().__init__(driver,expected_capacity)
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.website = "Best Buy"
#         # self.expected_capacity = expected_capacity
#     def check_if_item_in_stock(self,driver):
#         print(driver)
#         try:
# #            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "waitCreate")))
#             #driver.find_element(By.XPATH, '//button[@class="c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"')
#
#             # We'll give it 10 seconds to appear before looking further.
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to Cart"]')))
#             driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
#             self.in_stock = True
#         except Exception as e:
#             print("Class is not available on the page; no Add to Cart button")
#             print("Item is for NOT sale currently")
#             self.successfully_found_element = False
#             # print(e)
#
#         return self.in_stock
#     def get_price_of_item(self,driver):
#         price = ""
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//div[@class="priceView-hero-price priceView-customer-price"]')
#             self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             # print(e)
#         return self.price
#     def get_capactity_of_item(self,driver):
#         price = ""
#         try:
#             # driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
#             title_of_product = driver.find_element(By.XPATH, '//div[@class="sku-title"]')
#
#         except Exception as e:
#             print("Cannot find title of product")
#             title_of_product = "0TB"
#             self.successfully_found_element = False
#             self.capacity = self.expected_capacity
#             # print(e)
#
#         capacity = (re.search(r'\d+TB', title_of_product.text)).group() #12TB
#         # strip out the TB from the 12TB so that it's just a string of an integer
#         self.capacity = (re.search(r'\d+', capacity)).group() #12
#
#         return self.capacity
#
# class itemAmazon(itemWebsite):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.website = "Amazon"
#     def check_if_item_in_stock(self,driver):
#         print(driver)
#         try:
#             #driver.find_element(By.XPATH, '//button[@class="c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"')
#             # We'll give it 10 seconds to appear before looking further.
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="add-to-cart-button"]')))
#             driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]')
#             self.in_stock = True
#         except Exception as e:
#             print("Class is not available on the page; no Add to Cart button")
#             print("Item is for NOT sale currently")
#             self.successfully_found_element = False
#             # print(e)
#
#         return self.in_stock
#     def get_price_of_item(self,driver):
#         price = ""
#
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]')
#             print("first price")
#             whole_number, decimal_number = what_I_found.text.split('\n')
#             print(whole_number)
#             print(decimal_number)
#             price = whole_number + "." + decimal_number
#             print("price")
#             print(price)
#             # $538.86 (an example output)
#
#         except Exception as e:
#             try:
#                 what_I_found = driver.find_element(By.XPATH,'//span[@id="sns-base-price"]')
#                 print("second price")
#                 print(what_I_found.text)
#                 pattern = r'\$\d+\.\d+'  # Regular expression pattern to match the dollar amount
#                 dollar_search = re.search(pattern, what_I_found.text)  # Search for the pattern in the sentence
#                 print("dollar_search")
#                 print(dollar_search)
#                 # if dollar_search:
#                     # print("1")
#                 price = dollar_search.group()  # Get the matched portion
#                     # print("2")
#                     # print("dollar_amount_only")
#                 print(price)  # Output: $28.48
#                     # print("3")
#                 # else:
#                 #     print("No dollar amount found.")
#             except Exception as e:
#                 print("price is not available on the page Price")
#                 price = "$0.00" #Set a default price
#                 self.successfully_found_element = False
#                 # print(e)
#
#         # self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#         self.price = (re.search('\$(\d+,?\d*\.\d+)', price)).group(1)
#
#         # except Exception as e:
#         #     print("price is not available on the page Price")
#         #     self.successfully_found_element = False
#         #     # print(e)
#         # return self.price
#     def get_capactity_of_item(self,driver):
#         price = ""
#         try:
#             # driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
#             what_I_found = driver.find_element(By.XPATH, '//span[@id="productTitle"]')
#             # product_title = soup.find('div', {'class': 'shop-product-title'})
# #            self.capacity = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#             #            self.capacity = (re.search('([0-9]+TB$)\w+', what_I_found.text)).group(1)
#             # self.capacity = (re.search(r'\d+(?=TB)', what_I_found.text)).group(1)
#             # self.capacity = re.findall('([0-9]+)\w+', self.capacity)
#             self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
#             # strip out the TB from the 12TB so that it's just a string of an integer
#             self.capacity = (re.search(r'\d+', what_I_found.text)).group()
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             self.capacity = "0TB"
#             # print(e)
#
#         return self.capacity
#
#
# class itemBHPhoto(itemWebsite):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.website = "B&H Photo"
#
#
#     def check_for_if_page_is_redirected(self, driver):
#         try:
#             print("checking for alternative")
#             # If temporarily out of stock, BHPhoto gives an alternative product to look at, though can still click link to get it to the expected page.
#             what_I_found = driver.find_element(By.XPATH, '//span[@data-selenium="discontinuedItemShortDescription"]')
#             print("found it")
#
#             what_I_found.click
#             print("k")
#
#             # # element = driver.find_element_by_css_selector('#px-captcha')
#             # action = ActionChains(driver)
#             # action.click_and_hold(what_I_found)
#             # action.perform()
#
#
#             print("what_I_found")
#             print(what_I_found.text)
#         except Exception as e:
#             print("alternative Wasn't Found")
#             # no press & hold button
#             pass
#         return 0
#
#     def check_for_captcha(self, driver):
#
#         try:
#             # time.sleep(1000)
#             # time.sleep(5)
#             print("trying to find hold button on BH Photo Page")
#     #        element = driver.find_element_by_css_selector('#px-captcha-error-button')
#     #         element = driver.find_element(By.XPATH, '//div[@class="px-captcha-error-button"]')
#     #         element = driver.find_element(By.XPATH, '//div[@class="px-captcha-error-button"]')
#
#
#             ## CLOSEST TO WORKING
#             #Having to do the following because the Press & Hold button is dynamically created with a unique ID each time the page is generated and generated with an innerHTML
# #           element = driver.find_elements(By.XPATH, '//*[text()[contains(.,"Press & Hold")]]')
#
#
#
#             # # Get the page content
#             page_content = driver.page_source
#             page_content_soup = BeautifulSoup(page_content, 'lxml')
#
#             # print("page_content_soup")
#             # print(page_content_soup)
#     #
#     #
#     #         ## Give time for iframe to load ##
#     #         # time.sleep(3000)
#     #
#     #         iframes = driver.find_elements_by_xpath("//iframe")
#     #         print("0")
#     #         for index, iframe in enumerate(iframes):
#     #             # Your sweet business logic applied to iframe goes here.
#     #             print("1")
#     #             driver.switch_to.frame(index)
#     #             print("2")
#     #             find_all_iframes(driver)
#     #             print("3")
#     #             driver.switch_to.parent_frame()
#     #             print("4")
#     #
#     #         print("hmmmmmmm")
#     #
#     #
#     #         ## You have to switch to the iframe like so: ##
#     #
#     #         WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
#     #             (By.XPATH, "//iframe[starts-with(@style, 'display: block')]")))
#     #         print("hmmmmmm")
#     #
#     #
#     #         element = driver.find_element(By.CLASS_NAME, 'px-captcha-error-button')
#     #         print(len(WebDriverWait(element, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))))
#     #         print("Hmmm")
#     #
#     #         elem = driver.find_element(By.XPATH, "//iframe[contains(@style,'display: block')]")
#     #         print("found the iFram with style")
#     #         print(elem)
#     #
#     #         driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#     #
#     #         WebDriverWait(driver, 10).until(
#     #             EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[style='display:none'']")))
#     #         print("switched to iFrame")
#     #
#     #         # l = driver.find_element_by_css_selector("h4")
#     #         element = driver.find_element(by.CLASS_NAME, 'px-captcha-error-button')
#     #         # print("HTML code of element: " + l.get_attribute('innerHTML'))
#     #
#     #
#     #         # element = driver.find_element(By.XPATH, '//*[class()[contains(.,"px-captcha-error-button")]]')
#     #
#     #
#     #         #element = html.find_element(By.XPATH,"//*[text()='Press & Hold']").get_attribute("innerHTML")
#     #
#     #         # pageSource = driver.find_element_by_xpath("//*")
#     #         #
#     #         print("element")
#     #
#     #         for each in element:
#     #             print(each.text)
#     #         # print(element.text)
#     # #        element = driver.find_element(By.XPATH, '//div[@class="px-captcha-error-header"]')
#     # #        element = driver.find_element_by_css_selector('px-captcha-error-button')
#     #         print("found hold button")
#     #         # time.sleep(100)
#     #         action = ActionChains(driver)
#     #         action.click_and_hold(element)
#     #         action.perform()
#     #         time.sleep(10)
#     #         action.release(element)
#     #         action.perform()
#     #         time.sleep(0.2)
#     #         action.release(element)
#         except Exception as e:
#             print("Hold Button Wasn't Found")
#             #no press & hold button
#             pass
#
#         return 0
#
#     def check_if_item_in_stock(self,driver):
#         print(driver)
#         try:
#             #BH Photo sometimes has Add to Cart buttons, but also has "Out of Stock" text on those pages, too.
#             #Not truly in stock
#
#             WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to Cart"]')))
#             driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
#             self.in_stock = True
#         except Exception as e:
#             print("Class is not available on the page")
#             print("Item is for NOT sale currently")
#             self.successfully_found_element = False
#             time.sleep(10)
# #            print(e)
#
#         #Even if Add to Cart is present, sometimes "Temporarily Out of Stock" comes up
#         print("trying temp out of stock text")
#         try:
#             driver.find_element(By.XPATH, '//span[contains(text(),"Temporarily Out of Stock")]')
#             self.in_stock = False
#             print("Item is for NOT sale currently")
#         except Exception as e:
#             print("there is NOT a Temporarily Out of Stock on the page, so it must be in stock")
#             self.successfully_found_element = False
#             time.sleep(10)
#
#         return self.in_stock
#
#     def get_price_of_item(self,driver):
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//div[@class="price_L0iytPTSvv"]')
#             self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             self.price="0.00"
#             time.sleep(10)
# #            print(e)
#         return self.price
#
#     def get_capactity_of_item(self, driver):
#         price = ""
#         try:
#             #This is the element found when the normal webpage is found for it
#             HDD_Capacity_Sentence = driver.find_element(By.XPATH, '//h1[@data-selenium="productTitle"]')
#             print("This was from Main product page")
#         except Exception as e:
#             try:
#                 # This is the element found when product is temporarily out of stock and they offer up an alternate
#                 # product to buy (e.g. 18TB out of stock, look at the 20TB)
#                 HDD_Capacity_Sentence = driver.find_element(By.XPATH, '//a[@data-selenium="discontinuedItemNameLink"]')
#                 print("This was Out of Stock. Alternate product suggested")
#             except Exception as e:
#                 # nothing was found, better fill in a default value of 0
#                 print("Capacity Sentence Not Found On Page")
#                 HDD_Capacity_Sentence = "0TB"
#                 # self.capacity = self.expected_capacity
#                 # print(e)
#
#         capacity_with_TB = (re.search(r'\d+TB', HDD_Capacity_Sentence.text)).group() #12TB
#
#         # strip out the TB from the 12TB so that it's just a string of an integer
#         self.capacity = (re.search(r'\d+', capacity_with_TB)).group() #12
#
#         return self.capacity
#
# class itemNewEgg(itemWebsite):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.website = "NewEgg"
#
#     def check_if_item_in_stock(self,driver):
#         print(driver)
#         try:
#             # page_source.find_element(By.XPATH, '//button[text()="Add to Cart"]')
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to cart"]')))
#             driver.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
#             self.in_stock = True
#         except Exception as e:
#             print("Class is not available on the page")
#             print("Item is for NOT sale currently")
#             self.successfully_found_element = False
#             # print(e)
#
#         return self.in_stock
#     def get_price_of_item(self,driver):
#         try:
#             #
#             # '//button[normalize-space()="Add to Cart"]')
#             what_I_found = driver.find_element(By.XPATH, '//li[@class="price-current"]')
#             print("what_I_found")
#             print(what_I_found.text)
#             self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             # print(e)
#
#         return self.price
#
#     def get_capactity_of_item(self, driver):
#         price = ""
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//h1[@class="product-title"]')
#             self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             self.capacity = "0TB"
#             # print(e)
#
#         # strip out the TB from the 12TB so that it's just a string of an integer
#         self.capacity = (re.search(r'\d+', what_I_found.text)).group()
#
#         return self.capacity
#
# class itemWalmart:
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.website = "Walmart"
#     def check_for_captcha(self,driver):
#         element = driver.find_element_by_css_selector('#px-captcha')
#         action = ActionChains(driver)
#         action.click_and_hold(element)
#         action.perform()
#         time.sleep(10)
#         action.release(element)
#         action.perform()
#         time.sleep(0.2)
#         action.release(element)
#         return 0
#
#     def check_if_item_in_stock(self,driver):
#
#         print(driver)
#         try:
#             # page_source.find_element(By.XPATH, '//button[text()="Add to cart"]')
#             WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to cart"]')))
#             driver.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
#             #https://www.geeksforgeeks.org/python-selenium-find-button-by-text/
#             #Note: It is recommended to use normalize-space() method because it trim the left and right side spaces. It is possible that there can be spaces present at the start or at the end of the target text.
#
#             print("reached here")
#             self.in_stock = True
#         except Exception as e:
#             print("Class is not available on the page")
#             print("Item is for NOT sale currently")
#             self.successfully_found_element = False
#             # print(e)
#
#         return self.in_stock
#
#     def get_price_of_item(self,driver):
#
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//span[@itemprop="price"]')
#             self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
#
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             # print(e)
#
#         return self.price
#
#     def get_capactity_of_item(self, driver):
#         price = ""
#         try:
#             what_I_found = driver.find_element(By.XPATH, '//h1[@class="b lh-copy dark-gray mt1 mb2 f6 f3-m"]')
#             self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
#         except Exception as e:
#             print("Class is not available on the page Price")
#             self.successfully_found_element = False
#             self.capacity = "0TB"
#             # print(e)
#
#         # strip out the TB from the 12TB so that it's just a string of an integer
#         self.capacity = (re.search(r'\d+', what_I_found.text)).group()
#
#         return self.capacity


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




#def scrape_web_page_for_source_code(driver, url, expected_capacity):
def scrape_web_page_for_source_code(driver, url):
    #def scrape_web_page_for_source_code(url):

    # # Navigate to the URL
    driver.get(url)

    # THIS DIDN'T DO MUCH (added explcict waits when looking for "add to cart" buttons
    # #due to timeouts, try this workaround that will maybe automatcially refresh?
    # try:
    #     driver.get(url)
    # except TimeoutException as ex:
    #     print(ex.Message)
    #     driver.navigate().refresh()

    # r = requests.get(url)
    # page_content = BeautifulSoup(r.content, features='xml')

    # # Get the page content
    page_content = driver.page_source
    page_content_soup = BeautifulSoup(page_content, 'lxml')

    # print("page_content_soup")
    # print(page_content_soup)

    # Find the button using text
#    driver.find_element_by_xpath('//button[normalize-space()="Click me!"]').click()


# ***********

    print("processing: " + url)

    if "bestbuy" in url:
        # print("bestbuy is in url")
#        hard_drive = itemBestBuy(driver, expected_capacity)
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

    # #first, check that there is no captcha on the page!!!
    hard_drive.check_for_captcha(driver)

    # stock_check = hard_drive.check_if_item_in_stock(driver)
    #
    # print("stock_check")
    # print(stock_check)
    #
    # item_price = hard_drive.get_price_of_item(driver)
    # print("item_price")
    # print(item_price)
    #
    #
    # item_capacity = hard_drive.get_capactity_of_item(driver)
    # print("item_capacity")
    # print(item_capacity)



    #All in one method; will get an instance of the element with:
    # website_store, model_number, item_description, capacity, price, in_stock, url
    # don't really need to return anything since it'll be the properties of that instance
    hard_drive.get_item_properties(driver)

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
    # options.add_argument('--proxy-server=proxy')
    # driver = uc.Chrome(options=options)


# Using regular chrome driver

    options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)

# Using undetected_chromedriver
#    driver = uc.Chrome(options=options)

    return driver


def close_the_driver(driver):
    # Close the driver
    driver.quit()
    print("driver closed")

    return 0

