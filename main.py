#!/usr/bin/python3
import ScrapeWebPage
import ReadInParametersFile
import ReadWriteDataToCSV
import ReadWriteDataToDB
import DetectPlatform

import time
import random
from random import randint
import inspect #for looking at attributes of obect/ class

from datetime import datetime #getting today's date
from selenium.common.exceptions import TimeoutException

# webdriver_auto_update.py For keeping chromedriver up to date *specifically for Raspberry Pi in order to get UC to work
# from webdriver_auto_update import check_driver



# Get a list of all the items to search for (by url)
list_of_urls = ReadInParametersFile.open_and_read_file()

#let's randomize the urls order so it maybe seems less of a bot
random.shuffle(list_of_urls)

#Open the driver for webscraping
driver = ScrapeWebPage.open_the_driver()


# For each of the urls read in, get the hard drive's details and put it in a HDD object instance.
list_of_hard_drive_items = []

# List to store the URLs that need to be retried
urls_to_retry = []

for each_url in list_of_urls:

    try:
        hard_drive_item, page_content_soup = ScrapeWebPage.scrape_web_page_for_source_code(driver, each_url)
        list_of_hard_drive_items.append(hard_drive_item)
        time.sleep(randint(2, 7)) # randomize a 2 to 7 second pause between websites (again, seem like less of a bot)

    except TimeoutException:
        urls_to_retry.append(url)  # Add the URL to the retry list

print("URLs that timed out (if any): ")
print(urls_to_retry)


# this should be one long list initially sorted by website name and then by capacity
list_of_HDDs_sorted_by_Website_then_Capacity = ReadWriteDataToCSV.sortListOfDevicesForOutput(list_of_hard_drive_items)

# Long list of prices. List is initially sorted by website_store, then by capacity.
list_of_prices = ReadWriteDataToCSV.list_of_prices_sorted_by_website_then_capacity(list_of_HDDs_sorted_by_Website_then_Capacity)

# write the list of HDD prices to the CSV file
ReadWriteDataToCSV.read_in_and_write_out_csv_file(list_of_prices)


# Database Stuff
# Create a harddrives table in the products2.db.sqlite3 database (if it doesn't already exist)
ReadWriteDataToDB.create_hdd_database()

# write the list of HDD instances to a database
todays_date = datetime.today().strftime('%Y-%m-%d')
for each_hdd in list_of_hard_drive_items:
    ReadWriteDataToDB.insert_into_HDD_database(todays_date,each_hdd)
