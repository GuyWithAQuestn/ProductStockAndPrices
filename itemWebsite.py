import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Classes
class itemWebsite:
    # def __init__(self, driver, expected_capacity):
    #     self.expected_capacity = expected_capacity
    def __init__(self, driver):
        # self.expected_capacity = expected_capacity
        self.current_url = driver.current_url #also want to store the URL to the current product
        self.capacity = '.'
        self.page_source = driver
        self.in_stock = False
        self.price = ".."
        self.website = "..."
        self.successfully_found_element = True
        self.item_description = "...."
        self.model_number = "....."

    def check_for_if_page_is_redirected(self, driver):
        #pages like BHPhoto will refer to another product when something isn't in stock.
        #leave this blank and just pass through in most circumstances
        pass
        return 0

    def check_for_captcha(self,driver):
        pass
        return 0

    def get_item_properties(self, driver):

        # Check to see if the item is in stock
        try:
            # We'll give it 10 seconds to appear before looking further.
            # Only doing on the first element as I assume the remaining elements will have loaded by the time this one has
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to Cart"]')))
            driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            self.in_stock = True
        except Exception as e:
            print("No Add button. Item is for NOT sale currently")
            self.in_stock = False
            # print(e)

        # Next, get the price of the item
        try:
            price_sentence = driver.find_element(By.XPATH, '//div[@class="priceView-hero-price priceView-customer-price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', price_sentence.text)).group(1)
        except Exception as e:
            # print(e)
            print("Class is not available on the page Price")
            self.price = "0.00"

        # What is the model number of the drive?
        try:
            model_number = driver.find_element(By.XPATH, '//div[@class="model product-data"]')
            pattern = r'(?<=:)[A-Z0-9-]+(?=\b)'  # Regular expression pattern to match the desired string
            model_number_group = re.search(pattern, model_number.text)  # Search for the pattern in the sentence
            self.model_number = model_number_group.group()
        except Exception as e:
            print("Cannot find model number of product")
            self.model_number = "Unknown Model"


        # What is the Description/ Capacity of the drive?
        try:
            title_of_product = driver.find_element(By.XPATH, '//div[@class="sku-title"]')
            self.item_description = title_of_product.text

            # From the title of the product, get the capacity
            capacity = (re.search(r'\d+TB', title_of_product.text)).group()  # 12TB
            # strip out the TB from the 12TB so that it's just a string of an integer
            self.capacity = (re.search(r'\d+', capacity)).group()  # 12

        except Exception as e:
            print("Cannot find title of product")
            self.item_description = "Unknown Description"
            self.capacity = "0"
            # print(e)

        return 0

class itemBestBuy(itemWebsite):
    # def __init__(self, driver,expected_capacity):
    #     super().__init__(driver,expected_capacity)
    def __init__(self, driver):
        super().__init__(driver)
        self.website = "Best Buy"
        # self.expected_capacity = expected_capacity

    def get_item_properties(self, driver):

        # Check to see if the item is in stock
        try:
            # We'll give it 10 seconds to appear before looking further.
            # Only doing on the first element as I assume the remaining elements will have loaded by the time this one has
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to Cart"]')))
            # driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            self.in_stock = True
        except Exception as e:
            print("No Add button. Item is for NOT sale currently")
            self.in_stock = False
            # print(e)

        # Next, get the price of the item
        try:
            price_sentence = driver.find_element(By.XPATH, '//div[@class="priceView-hero-price priceView-customer-price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', price_sentence.text)).group(1)
        except Exception as e:
            # print(e)
            print("Class is not available on the page Price")
            self.price = "0.00"

        # What is the model number of the drive?
        try:
            model_number = driver.find_element(By.XPATH, '//div[@class="model product-data"]')
            pattern = r'(?<=:)[A-Z0-9-]+(?=\b)'  # Regular expression pattern to match the desired string
            model_number_group = re.search(pattern, model_number.text)  # Search for the pattern in the sentence
            self.model_number = model_number_group.group()
        except Exception as e:
            print("Cannot find model number of product")
            self.model_number = "Unknown Model"


        # What is the Description/ Capacity of the drive?
        try:
            title_of_product = driver.find_element(By.XPATH, '//div[@class="sku-title"]')
            self.item_description = title_of_product.text

            # From the title of the product, get the capacity
            capacity = (re.search(r'\d+TB', title_of_product.text)).group()  # 12TB
            # strip out the TB from the 12TB so that it's just a string of an integer
            self.capacity = (re.search(r'\d+', capacity)).group()  # 12

        except Exception as e:
            print("Cannot find title of product")
            self.item_description = "Unknown Description"
            self.capacity = "0"
            # print(e)

        return 0

class itemAmazon(itemWebsite):
    def __init__(self, driver):
        super().__init__(driver)
        self.website = "Amazon"


    def get_item_properties(self, driver):

        # Check to see if the item is in stock
        try:
            # We'll give it 10 seconds to appear before looking further.
            # Only doing on the first element as I assume the remaining elements will have loaded by the time this one has
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//input[@id="add-to-cart-button"]')))
            driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]')
            self.in_stock = True
        except Exception as e:
            print("No Add button. Item is for NOT sale currently")
            self.in_stock = False
            # print(e)

        # Next, get the price of the item
        # For Amazon, the price can be in a few different spots, so  allowing it to check with multiple Try: statements
        try:
            what_I_found = driver.find_element(By.XPATH, '//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]')
            whole_number, decimal_number = what_I_found.text.split('\n')
            price = whole_number + "." + decimal_number # $538.86 (an example output)

        except Exception as e:
            try:
                what_I_found = driver.find_element(By.XPATH,'//span[@id="sns-base-price"]')
                pattern = r'\$\d+\.\d+'  # Regular expression pattern to match the dollar amount
                dollar_search = re.search(pattern, what_I_found.text)  # Search for the pattern in the sentence
                price = dollar_search.group()  # Get the matched portion
            except Exception as e:
                print("price is not available on the page Price")
                price = "$0.00" #Set a default price
                # print(e)
        self.price = (re.search('\$(\d+,?\d*\.\d+)', price)).group(1)


        # # What is the model number of the drive?
        # try:
        #     model_number = driver.find_element(By.XPATH, '//div[@class="model product-data"]')
        #     pattern = r'(?<=:)[A-Z0-9-]+(?=\b)'  # Regular expression pattern to match the desired string
        #     model_number_group = re.search(pattern, model_number.text)  # Search for the pattern in the sentence
        #     self.model_number = model_number_group.group()
        # except Exception as e:
        #     print("Cannot find model number of product")
        #     self.model_number = "Unknown Model"


        # What is the Description/ Capacity/ Model Number of the drive?
        try:
            # Title of product
            title_of_product = driver.find_element(By.XPATH, '//span[@id="productTitle"]')
            self.item_description = title_of_product.text

            # Capacity, from the title of the product
            capacity = (re.search(r'\d+TB', title_of_product.text)).group()  # 12TB
            # strip out the TB from the 12TB so that it's just a string of an integer
            self.capacity = (re.search(r'\d+', capacity)).group()  # 12

            #Model Number, from the title of the product
            pattern = r'\b[A-Z0-9-]{14,}\b'  # Regular expression pattern to match the desired string
            model_number_group = re.search(pattern, title_of_product.text)  # Search for the pattern in the sentence
            self.model_number = model_number_group.group()
        except Exception as e:
            print("Cannot find title of product")
            self.item_description = "Unknown Description"
            self.capacity = "0"
            self.model_number = "Unknown Model"
            # print(e)
        return 0

class itemBHPhoto(itemWebsite):
    def __init__(self, driver):
        super().__init__(driver)
        self.website = "B&H Photo"


    def check_for_if_page_is_redirected(self, driver):
        try:
            print("checking for alternative")
            # If temporarily out of stock, BHPhoto gives an alternative product to look at, though can still click link to get it to the expected page.
            what_I_found = driver.find_element(By.XPATH, '//span[@data-selenium="discontinuedItemShortDescription"]')
            print("found it")

            what_I_found.click
            print("k")

            # # element = driver.find_element_by_css_selector('#px-captcha')
            # action = ActionChains(driver)
            # action.click_and_hold(what_I_found)
            # action.perform()


            print("what_I_found")
            print(what_I_found.text)
        except Exception as e:
            print("alternative Wasn't Found")
            # no press & hold button
            pass
        return 0

    def check_for_captcha(self, driver):

        try:
            # time.sleep(1000)
            # time.sleep(5)
            print("trying to find hold button on BH Photo Page")
    #        element = driver.find_element_by_css_selector('#px-captcha-error-button')
    #         element = driver.find_element(By.XPATH, '//div[@class="px-captcha-error-button"]')
    #         element = driver.find_element(By.XPATH, '//div[@class="px-captcha-error-button"]')


            ## CLOSEST TO WORKING
            #Having to do the following because the Press & Hold button is dynamically created with a unique ID each time the page is generated and generated with an innerHTML
#           element = driver.find_elements(By.XPATH, '//*[text()[contains(.,"Press & Hold")]]')



            # # Get the page content
            page_content = driver.page_source
            page_content_soup = BeautifulSoup(page_content, 'lxml')

            # print("page_content_soup")
            # print(page_content_soup)
    #
    #
    #         ## Give time for iframe to load ##
    #         # time.sleep(3000)
    #
    #         iframes = driver.find_elements_by_xpath("//iframe")
    #         print("0")
    #         for index, iframe in enumerate(iframes):
    #             # Your sweet business logic applied to iframe goes here.
    #             print("1")
    #             driver.switch_to.frame(index)
    #             print("2")
    #             find_all_iframes(driver)
    #             print("3")
    #             driver.switch_to.parent_frame()
    #             print("4")
    #
    #         print("hmmmmmmm")
    #
    #
    #         ## You have to switch to the iframe like so: ##
    #
    #         WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it(
    #             (By.XPATH, "//iframe[starts-with(@style, 'display: block')]")))
    #         print("hmmmmmm")
    #
    #
    #         element = driver.find_element(By.CLASS_NAME, 'px-captcha-error-button')
    #         print(len(WebDriverWait(element, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "iframe")))))
    #         print("Hmmm")
    #
    #         elem = driver.find_element(By.XPATH, "//iframe[contains(@style,'display: block')]")
    #         print("found the iFram with style")
    #         print(elem)
    #
    #         driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    #
    #         WebDriverWait(driver, 10).until(
    #             EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[style='display:none'']")))
    #         print("switched to iFrame")
    #
    #         # l = driver.find_element_by_css_selector("h4")
    #         element = driver.find_element(by.CLASS_NAME, 'px-captcha-error-button')
    #         # print("HTML code of element: " + l.get_attribute('innerHTML'))
    #
    #
    #         # element = driver.find_element(By.XPATH, '//*[class()[contains(.,"px-captcha-error-button")]]')
    #
    #
    #         #element = html.find_element(By.XPATH,"//*[text()='Press & Hold']").get_attribute("innerHTML")
    #
    #         # pageSource = driver.find_element_by_xpath("//*")
    #         #
    #         print("element")
    #
    #         for each in element:
    #             print(each.text)
    #         # print(element.text)
    # #        element = driver.find_element(By.XPATH, '//div[@class="px-captcha-error-header"]')
    # #        element = driver.find_element_by_css_selector('px-captcha-error-button')
    #         print("found hold button")
    #         # time.sleep(100)
    #         action = ActionChains(driver)
    #         action.click_and_hold(element)
    #         action.perform()
    #         time.sleep(10)
    #         action.release(element)
    #         action.perform()
    #         time.sleep(0.2)
    #         action.release(element)
        except Exception as e:
            print("Hold Button Wasn't Found")
            #no press & hold button
            pass

        return 0

    def check_if_item_in_stock(self,driver):
        print(driver)
        try:
            #BH Photo sometimes has Add to Cart buttons, but also has "Out of Stock" text on those pages, too.
            #Not truly in stock

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to Cart"]')))
            driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page")
            print("Item is for NOT sale currently")
            self.successfully_found_element = False
            time.sleep(10)
#            print(e)

        #Even if Add to Cart is present, sometimes "Temporarily Out of Stock" comes up
        print("trying temp out of stock text")
        try:
            driver.find_element(By.XPATH, '//span[contains(text(),"Temporarily Out of Stock")]')
            self.in_stock = False
            print("Item is for NOT sale currently")
        except Exception as e:
            print("there is NOT a Temporarily Out of Stock on the page, so it must be in stock")
            self.successfully_found_element = False
            time.sleep(10)

        return self.in_stock

    def get_price_of_item(self,driver):
        try:
            what_I_found = driver.find_element(By.XPATH, '//div[@class="price_L0iytPTSvv"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            self.price="0.00"
            time.sleep(10)
#            print(e)
        return self.price

    def get_capactity_of_item(self, driver):
        price = ""
        try:
            #This is the element found when the normal webpage is found for it
            HDD_Capacity_Sentence = driver.find_element(By.XPATH, '//h1[@data-selenium="productTitle"]')
            print("This was from Main product page")
        except Exception as e:
            try:
                # This is the element found when product is temporarily out of stock and they offer up an alternate
                # product to buy (e.g. 18TB out of stock, look at the 20TB)
                HDD_Capacity_Sentence = driver.find_element(By.XPATH, '//a[@data-selenium="discontinuedItemNameLink"]')
                print("This was Out of Stock. Alternate product suggested")
            except Exception as e:
                # nothing was found, better fill in a default value of 0
                print("Capacity Sentence Not Found On Page")
                HDD_Capacity_Sentence = "0TB"
                # self.capacity = self.expected_capacity
                # print(e)

        capacity_with_TB = (re.search(r'\d+TB', HDD_Capacity_Sentence.text)).group() #12TB

        # strip out the TB from the 12TB so that it's just a string of an integer
        self.capacity = (re.search(r'\d+', capacity_with_TB)).group() #12

        return self.capacity

class itemNewEgg(itemWebsite):
    def __init__(self, driver):
        super().__init__(driver)
        self.website = "NewEgg"

    def get_item_properties(self, driver):
        # Check to see if the item is in stock
        try:
            # We'll give it 10 seconds to appear before looking further.
            # Only doing on the first element as I assume the remaining elements will have loaded by the time this one has
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to cart"]')))
            driver.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
            self.in_stock = True
        except Exception as e:
            print("No Add button. Item is for NOT sale currently")
            self.in_stock = False
            # print(e)

        # Next, get the price of the item
        # For Amazon, the price can be in a few different spots, so  allowing it to check with multiple Try: statements
        try:
            price_element = driver.find_element(By.XPATH, '//li[@class="price-current"]')
            price = price_element.text
            # whole_number, decimal_number = what_I_found.text.split('\n')
            # price = whole_number + "." + decimal_number  # $538.86 (an example output)
            # print(price)
        except Exception as e:
            print("price is not available on the page Price")
            price = "$0.00"  # Set a default price
            # print(e)
        self.price = (re.search('\$(\d+,?\d*\.\d+)', price)).group(1)

        # # What is the model number of the drive?
        # try:
        #     model_number = driver.find_element(By.XPATH, '//div[@class="model product-data"]')
        #     pattern = r'(?<=:)[A-Z0-9-]+(?=\b)'  # Regular expression pattern to match the desired string
        #     model_number_group = re.search(pattern, model_number.text)  # Search for the pattern in the sentence
        #     self.model_number = model_number_group.group()
        # except Exception as e:
        #     print("Cannot find model number of product")
        #     self.model_number = "Unknown Model"

        # What is the Description/ Capacity/ Model Number of the drive?
        try:
            # Title of product
            title_of_product = driver.find_element(By.XPATH, '//h1[@class="product-title"]')
            self.item_description = title_of_product.text

            # Capacity, from the title of the product
            capacity = (re.search(r'\d+TB', title_of_product.text)).group()  # 12TB
            # strip out the TB from the 12TB so that it's just a string of an integer
            self.capacity = (re.search(r'\d+', capacity)).group()  # 12

            # Model Number, from the title of the product
            pattern = r'\b[A-Z0-9-]{14,}\b'  # Regular expression pattern to match the desired string
            model_number_group = re.search(pattern, title_of_product.text)  # Search for the pattern in the sentence
            self.model_number = model_number_group.group()
        except Exception as e:
            print("Cannot find title of product")
            self.item_description = "Unknown Description"
            self.capacity = "0"
            self.model_number = "Unknown Model"
            # print(e)
        return 0

class itemWalmart:
    def __init__(self, driver):
        super().__init__(driver)
        self.website = "Walmart"
    def check_for_captcha(self,driver):
        element = driver.find_element_by_css_selector('#px-captcha')
        action = ActionChains(driver)
        action.click_and_hold(element)
        action.perform()
        time.sleep(10)
        action.release(element)
        action.perform()
        time.sleep(0.2)
        action.release(element)
        return 0



    def get_item_properties(self, driver):
        # Check to see if the item is in stock
        try:
            # We'll give it 10 seconds to appear before looking further.
            # Only doing on the first element as I assume the remaining elements will have loaded by the time this one has
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to cart"]')))
            driver.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
            self.in_stock = True
        except Exception as e:
            print("No Add button. Item is for NOT sale currently")
            self.in_stock = False
            # print(e)

        # Next, get the price of the item
        # For Amazon, the price can be in a few different spots, so  allowing it to check with multiple Try: statements
        try:
            price = driver.find_element(By.XPATH, '//span[@itemprop="price"]')
        except Exception as e:
            print("price is not available on the page Price")
            price = "$0.00"  # Set a default price
            # print(e)
        self.price = (re.search('\$(\d+,?\d*\.\d+)', price)).group(1)

        # # What is the model number of the drive?
        # try:
        #     model_number = driver.find_element(By.XPATH, '//div[@class="model product-data"]')
        #     pattern = r'(?<=:)[A-Z0-9-]+(?=\b)'  # Regular expression pattern to match the desired string
        #     model_number_group = re.search(pattern, model_number.text)  # Search for the pattern in the sentence
        #     self.model_number = model_number_group.group()
        # except Exception as e:
        #     print("Cannot find model number of product")
        #     self.model_number = "Unknown Model"

        # What is the Description/ Capacity/ Model Number of the drive?
        try:
            # Title of product
            title_of_product = driver.find_element(By.XPATH, '//h1[@class="b lh-copy dark-gray mt1 mb2 f6 f3-m mh0-l mh3"]')
            self.item_description = title_of_product.text

            # Capacity, from the title of the product
            capacity = (re.search(r'\d+TB', title_of_product.text)).group()  # 12TB
            # strip out the TB from the 12TB so that it's just a string of an integer
            self.capacity = (re.search(r'\d+', capacity)).group()  # 12

            # Model Number, from the title of the product
            pattern = r'\b[A-Z0-9-]{14,}\b'  # Regular expression pattern to match the desired string
            model_number_group = re.search(pattern, title_of_product.text)  # Search for the pattern in the sentence
            self.model_number = model_number_group.group()
        except Exception as e:
            print("Cannot find title of product")
            self.item_description = "Unknown Description"
            self.capacity = "0"
            self.model_number = "Unknown Model"
            # print(e)
        return 0
