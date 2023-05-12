import sqlite3
from ScrapeWebPage import itemWebsite
from ScrapeWebPage import itemAmazon
from ScrapeWebPage import itemBestBuy
from ScrapeWebPage import itemBHPhoto
from ScrapeWebPage import itemNewEgg
from ScrapeWebPage import itemWalmart



conn = sqlite3.connect('products.db')

c = conn.cursor()

# TABLE ALREADY EXISTS NOW
# c.execute("""CREATE TABLE harddrives (
#             date text,
#             url text,
#             website_store text,
#             capacity text,
#             price text,
#             description text,
#             in_stock text
#             )""")

# c.execute("""INSERT INTO harddrives VALUES (
#             '2023-05-11',
#             'https://www.bestbuy.com/site/wd-easystore-22tb-external-usb-3-0-hard-drive-black/6537414.p?skuId=6537414#anchor=productVariations',
#             'best buy',
#             '22TB',
#             '499.99',
#             'WD - easystore 22TB External USB 3.0 Hard Drive - Black',
#             'yes'
#             )""")

# conn.commit()

c.execute("""SELECT * FROM harddrives WHERE website_store='best buy'""")

# c.fetchone()
# c.fetchmany(5)
print(c.fetchall())

conn.commit()
conn.close()
