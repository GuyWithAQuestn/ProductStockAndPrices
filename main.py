import ScrapeWebPage
import ReadInParametersFile
import ReadWriteDataToCSV
import ReadWriteDataToDB

import time
import random
from random import randint
import inspect #for looking at attributes of obect/ class

from datetime import datetime #getting today's date





#from bs4 import BeautifulSoup

# url = 'https://www.bestbuy.com/site/wd-easystore-22tb-external-usb-3-0-hard-drive-black/6537414.p?skuId=6537414#anchor=productVariations'
#url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-4070-12gb-gddr6x-graphics-card-titanium-and-black/6539358.p?skuId=6539358'

# url = 'https://www.bestbuy.com/site/wd-easystore-18tb-external-usb-3-0-hard-drive-black/6427995.p?skuId=6427995'
#url = 'https://www.bhphotovideo.com/c/product/1719161-REG/wd_wdbwlg0200hbk_nesn_elements_desktop_external_hard.html'
#url = 'https://www.bhphotovideo.com/c/product/1559485-REG/seasonic_electronics_prime_fanless_tx_700_700w.html'
# url = 'https://www.bestbuy.com/site/wd-red-pro-14tb-internal-sata-nas-hard-drive-for-desktops/6523106.p?skuId=6523106#anchor=productVariations'
# url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-4070-12gb-gddr6x-graphics-card-titanium-and-black/6539358.p?skuId=6539358'
#url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
#url = 'https://www.walmart.com/ip/Western-Digital-0F38459SP-3-5-in-Ultra-Star-18TB-26-1-mm-512MB-7200RPM-DC-HC550-Internal-Hard-Drive/794882883?from=searchResults'

# url = 'http://www.whatismyproxy.com/'

# # ****
# #for sorting lists of hard drives
# def getKeyPrice(obj):
#     return obj.price
#
# def getKeyWebsite(obj):
#     return obj.website
#
# def getKeyCapacity(obj):
#     return int(obj.capacity)
# # ****

list_of_urls = ReadInParametersFile.open_and_read_file()

#let's randomize the urls order so it maybe seems less of a bot
random.shuffle(list_of_urls)

#Open the driver for webscraping
driver = ScrapeWebPage.open_the_driver()

list_of_hard_drive_items = []

# For each of the urls read in, get the hard drive's details and put it in a HDD object instance.
# iteration = 1

for each_url in list_of_urls:
    # print("This is item number: " + str(iteration))
    # iteration += 1

    # expected_capacity, url = each_url.split(',')

    # print("url")
    # print(url)
    # print("expected_capacity")
    # print(expected_capacity)

    # hard_drive_item, page_content_soup = ScrapeWebPage.scrape_web_page_for_source_code(driver, url, expected_capacity)
    hard_drive_item, page_content_soup = ScrapeWebPage.scrape_web_page_for_source_code(driver, each_url)
    list_of_hard_drive_items.append(hard_drive_item)
    print("hard_drive_item.successfully_found_element")
    print(str(hard_drive_item.successfully_found_element))
    time.sleep(randint(3, 10))


# print("list_of_hard_drive_items")
# print(list_of_hard_drive_items)


# this should be one long list initially sorted by website name and then by capacity
list_of_HDDs_sorted_by_Website_then_Capacity = ReadWriteDataToCSV.sortListOfDevicesForOutput(list_of_hard_drive_items)
print("list_of_HDDs_sorted_by_Website_then_Capacity")
print(list_of_HDDs_sorted_by_Website_then_Capacity)

list_of_prices = ReadWriteDataToCSV.list_of_prices_sorted_by_website_then_capacity(list_of_HDDs_sorted_by_Website_then_Capacity)

ReadWriteDataToCSV.read_in_and_write_out_csv_file(list_of_prices)

todays_date = datetime.today().strftime('%Y-%m-%d')
print("each_hdd instance:")
i=1
for each_hdd in list_of_hard_drive_items:
    print("item: " + str(i))
    i=i+1
    ReadWriteDataToDB.insert_into_HDD_database(todays_date,each_hdd)

# what do I have in terms of objects/ instances that I've scraped
print("each_hdd instance:")
i=1
for each_hdd in list_of_hard_drive_items:
    print("item: " + str(i))
    i=i+1
    print(each_hdd.website)
    print(each_hdd.capacity)
    print(each_hdd.price)
    print(each_hdd.in_stock)
    print(each_hdd.model_number)
    print(each_hdd.item_description)
    print(datetime.today().strftime('%Y-%m-%d'))
    print(each_hdd.current_url)


    # for each in each_item:
    #     print(each.website)
    #     print(each.cap)
    # print(each_item.website + ":" + each_item.capacity)


# for each_instance in list_of_hard_drive_items:
#     print(each_instance.website)
#     print(each_instance.capacity)
#     print(each_instance.price)
#     print(each_instance.in_stock)

# # method 1
# list_of_hard_drive_items.sort(key=getKeyPrice)
# print("Sort by Price")
# print(list_of_hard_drive_items)
#
# for each_instance in list_of_hard_drive_items:
#     print(each_instance.website)
#     print(each_instance.price)

# # method 1
# list_of_hard_drive_items.sort(key=getKeyWebsite)
# print("Sort by Website")
# print(list_of_hard_drive_items)
#
# for each_instance in list_of_hard_drive_items:
#     print(each_instance.website)
#     print(each_instance.price)
#
#     # print("page_content_soup")
#     # print(page_content_soup)


# # ****
#
#
# # since each of the URLs were accessed randomly (to help decrease chances of being detected as a bot)
# # Going to group each of the hard drives by their website name
# # create a unique list of website names
# unique_list_of_websites = []
#
# for each_instance in list_of_hard_drive_items:
#      # print(each_instance.website)
#      # print(each_instance.price)
#      if each_instance.website not in unique_list_of_websites:
#          unique_list_of_websites.append(each_instance.website)
#
# print("unique_list_of_websites")
# print(unique_list_of_websites)
#
#
# # For each website name, create a list within a list
# #[website nameA [list of drives prices], website nameB [list of drives prices], etc]
#
# master_list_of_prices_based_on_website = []
#
# for each_website in unique_list_of_websites:
#     master_list_of_prices = []
#
#     for each_instance in list_of_hard_drive_items:
#         if each_website == each_instance.website:
#             master_list_of_prices.append(each_instance.price)
#
#     master_list_of_prices_based_on_website.append(master_list_of_prices)
#
#
# list_iteration = 1
# for each_websites_prices in master_list_of_prices_based_on_website:
#     print("list_iteration")
#     print(list_iteration)
#     list_iteration = list_iteration + 1
#     print(each_websites_prices)
#
#
# # Sort hard drives by capacity (highest capacity to least capacity)
# list_of_hard_drive_items.sort(key=getKeyCapacity,reverse=True)
# print("Sort by Capacity")
# print(list_of_hard_drive_items)
#
# for each_instance in list_of_hard_drive_items:
#     print(each_instance.capacity)
#     print(each_instance.price)
#
# # *****