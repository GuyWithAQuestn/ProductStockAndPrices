import ScrapeWebPage
import ReadInParametersFile
import random


#from bs4 import BeautifulSoup

# url = 'https://www.bestbuy.com/site/wd-easystore-22tb-external-usb-3-0-hard-drive-black/6537414.p?skuId=6537414#anchor=productVariations'
#url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-4070-12gb-gddr6x-graphics-card-titanium-and-black/6539358.p?skuId=6539358'

url = 'https://www.bestbuy.com/site/wd-easystore-18tb-external-usb-3-0-hard-drive-black/6427995.p?skuId=6427995'
#url = 'https://www.bhphotovideo.com/c/product/1719161-REG/wd_wdbwlg0200hbk_nesn_elements_desktop_external_hard.html'
#url = 'https://www.bhphotovideo.com/c/product/1559485-REG/seasonic_electronics_prime_fanless_tx_700_700w.html'
# url = 'https://www.bestbuy.com/site/wd-red-pro-14tb-internal-sata-nas-hard-drive-for-desktops/6523106.p?skuId=6523106#anchor=productVariations'
# url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-4070-12gb-gddr6x-graphics-card-titanium-and-black/6539358.p?skuId=6539358'
#url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402'
#url = 'https://www.walmart.com/ip/Western-Digital-0F38459SP-3-5-in-Ultra-Star-18TB-26-1-mm-512MB-7200RPM-DC-HC550-Internal-Hard-Drive/794882883?from=searchResults'

list_of_urls = ReadInParametersFile.open_and_read_file()

#let's randomize the urls order so it maybe seems less of a bot
random.shuffle(list_of_urls)

# print("list_of_urls")
# print(list_of_urls)

driver = ScrapeWebPage.open_the_driver()

list_of_hard_drive_items = []

iteration = 1
for each_url in list_of_urls:
    print("This is item number: " + str(iteration))
    iteration += 1
    hard_drive_item, page_content_soup = ScrapeWebPage.scrape_web_page_for_source_code(driver, each_url)
    list_of_hard_drive_items.append(hard_drive_item)

print("list_of_hard_drive_items")
print(list_of_hard_drive_items)

for each_instance in list_of_hard_drive_items:
    print(each_instance.website)
    print(each_instance.capacity)
    print(each_instance.price)
    print(each_instance.in_stock)

    # print("page_content_soup")
    # print(page_content_soup)


# print("page_content_soup")
# print(page_content_soup)