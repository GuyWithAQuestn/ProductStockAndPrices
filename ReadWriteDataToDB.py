import sqlite3
from ScrapeWebPage import itemWebsite
from ScrapeWebPage import itemAmazon
from ScrapeWebPage import itemBestBuy
from ScrapeWebPage import itemBHPhoto
from ScrapeWebPage import itemNewEgg
from ScrapeWebPage import itemWalmart

def create_hdd_database():

    conn = sqlite3.connect('products2.db.sqlite3')
    c = conn.cursor()

    sql_command_create_table = """CREATE TABLE IF NOT EXISTS harddrives (
        date TEXT,
        model_number TEXT,
        item_description TEXT,
        capacity TEXT,
        price TEXT,
        in_stock TEXT,
        website_store TEXT,
        url TEXT,
        PRIMARY KEY(date, model_number, website_store))"""

    c.execute(sql_command_create_table)
    conn.commit()
    conn.close()

    return 0



# TO GET RID OF TABLE
#c.execute("""DROP TABLE harddrives""")

# TABLE ALREADY EXISTS NOW
# c.execute("""CREATE TABLE harddrives (
#             date text,
#             model_number text,
#             item_description text,
#             capacity text,
#             price text,
#             in_stock text,
#             website_store text,
#             url text
#             )""")
#
# c.execute("""INSERT INTO harddrives VALUES (
#             '2023-05-11',
#             'WDBAMA0220HBK-NESN',
#             'WD - easystore 22TB External USB 3.0 Hard Drive - Black',
#             '22TB',
#             '499.99',
#             'yes',
#             'best buy',
#             'https://www.bestbuy.com/site/wd-easystore-22tb-external-usb-3-0-hard-drive-black/6537414.p?skuId=6537414#anchor=productVariations'
#             )""")

# conn.commit()

# c.execute("""SELECT * FROM harddrives""")
#
# # c.fetchone()
# # c.fetchmany(5)
# print(c.fetchall())
#
# conn.commit()
# conn.close()

def insert_into_HDD_database(date, itemWebsite):
    conn = sqlite3.connect('products2.db.sqlite3')

    c = conn.cursor()

    items_to_insert = (date,
                       itemWebsite.model_number,
                       itemWebsite.item_description,
                       itemWebsite.capacity,
                       itemWebsite.price,
                       itemWebsite.in_stock,
                       itemWebsite.website,
                       itemWebsite.current_url)

#    sql_commend = """INSERT INTO harddrives(DATE,MODEL_NUMBER,ITEM_DESCRIPTION,CAPACITY,PRICE,IN_STOCK,WEBSITE_STORE,URL)
#            VALUES(?,?,?,?,?,?,?,?)"""

    # https://www.sqlitetutorial.net/sqlite-replace-statement/
    # REPLACE will perfom an INSERT or REPLACE based on if there's already something there with unique data or not
    sql_commend = """REPLACE INTO harddrives(DATE,MODEL_NUMBER,ITEM_DESCRIPTION,CAPACITY,PRICE,IN_STOCK,WEBSITE_STORE,URL)
            VALUES(?,?,?,?,?,?,?,?)"""

    c.execute(sql_commend,items_to_insert)

    conn.commit()
    conn.close()

    return 0