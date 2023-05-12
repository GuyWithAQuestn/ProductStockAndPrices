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
        self.capacity = '.'
        self.page_source = driver
        self.in_stock = False
        self.price = ".."
        self.website = "..."
        self.successfully_found_element = True

    def check_for_if_page_is_redirected(self, driver):
        #pages like BHPhoto will refer to another product when something isn't in stock.
        #leave this blank and just pass through in most circumstances
        pass
        return 0

    def check_for_captcha(self,driver):
        pass
        return 0
    def check_if_item_in_stock(self,driver):
        print(driver)
        try:
            driver.find_element(By.XPATH, '//button[text()="Add to Cart"]')
            #driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page; no Add to Cart button")
            print("Item is for NOT sale currently")
            # print(e)
            self.successfully_found_element = False

        return self.in_stock

    def get_price_of_item(self,driver):
        # price = ""
        try:
            what_I_found = driver.find_element(By.XPATH, '//div[@class="price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        except Exception as e:
            print("Class is not available on the page Price")
            # print(e)
            self.successfully_found_element = False

        return self.price

    def get_capactity_of_item(self, driver):
        price = ""
        try:
            what_I_found = driver.find_element(By.XPATH, '//h1[@class="heading-5 v-fw-regular"]')
            self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            self.capacity = self.expected_capacity
            # print(e)

        # strip out the TB from the 12TB so that it's just a string of an integer
        self.capacity = (re.search(r'\d+', what_I_found.text)).group()

        return self.capacity

class itemBestBuy(itemWebsite):
    # def __init__(self, driver,expected_capacity):
    #     super().__init__(driver,expected_capacity)
    def __init__(self, driver):
        super().__init__(driver)
        self.website = "Best Buy"
        # self.expected_capacity = expected_capacity
    def check_if_item_in_stock(self,driver):
        print(driver)
        try:
#            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "waitCreate")))
            #driver.find_element(By.XPATH, '//button[@class="c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"')

            print("Checking for add button")
            # We'll give it 10 seconds to appear before looking further.
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to Cart"]')))
            driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page; no Add to Cart button")
            print("Item is for NOT sale currently")
            self.successfully_found_element = False
            # print(e)

        return self.in_stock
    def get_price_of_item(self,driver):
        price = ""
        try:
            what_I_found = driver.find_element(By.XPATH, '//div[@class="priceView-hero-price priceView-customer-price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            # print(e)
        return self.price
    def get_capactity_of_item(self,driver):
        price = ""
        try:
            # driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            title_of_product = driver.find_element(By.XPATH, '//div[@class="sku-title"]')

        except Exception as e:
            print("Cannot find title of product")
            title_of_product = "0TB"
            self.successfully_found_element = False
            self.capacity = self.expected_capacity
            # print(e)

        capacity = (re.search(r'\d+TB', title_of_product.text)).group() #12TB
        # strip out the TB from the 12TB so that it's just a string of an integer
        self.capacity = (re.search(r'\d+', capacity)).group() #12

        return self.capacity

class itemAmazon(itemWebsite):
    def __init__(self, driver):
        super().__init__(driver)
        self.website = "Amazon"
    def check_if_item_in_stock(self,driver):
        print(driver)
        try:
            #driver.find_element(By.XPATH, '//button[@class="c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button"')
            # We'll give it 10 seconds to appear before looking further.
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="add-to-cart-button"]')))
            driver.find_element(By.XPATH, '//input[@id="add-to-cart-button"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page; no Add to Cart button")
            print("Item is for NOT sale currently")
            self.successfully_found_element = False
            # print(e)

        return self.in_stock
    def get_price_of_item(self,driver):
        price = ""

        try:
            what_I_found = driver.find_element(By.XPATH, '//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]')
            print("first price")
            whole_number, decimal_number = what_I_found.text.split('\n')
            print(whole_number)
            print(decimal_number)
            price = whole_number + "." + decimal_number
            print("price")
            print(price)
            # $538.86 (an example output)

        except Exception as e:
            try:
                what_I_found = driver.find_element(By.XPATH,'//span[@id="sns-base-price"]')
                print("second price")
                print(what_I_found.text)
                pattern = r'\$\d+\.\d+'  # Regular expression pattern to match the dollar amount
                dollar_search = re.search(pattern, what_I_found.text)  # Search for the pattern in the sentence
                print("dollar_search")
                print(dollar_search)
                # if dollar_search:
                    # print("1")
                price = dollar_search.group()  # Get the matched portion
                    # print("2")
                    # print("dollar_amount_only")
                print(price)  # Output: $28.48
                    # print("3")
                # else:
                #     print("No dollar amount found.")
            except Exception as e:
                print("price is not available on the page Price")
                price = "$0.00" #Set a default price
                self.successfully_found_element = False
                # print(e)

        # self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        self.price = (re.search('\$(\d+,?\d*\.\d+)', price)).group(1)

        # except Exception as e:
        #     print("price is not available on the page Price")
        #     self.successfully_found_element = False
        #     # print(e)
        # return self.price
    def get_capactity_of_item(self,driver):
        price = ""
        try:
            # driver.find_element(By.XPATH, '//button[normalize-space()="Add to Cart"]')
            what_I_found = driver.find_element(By.XPATH, '//span[@id="productTitle"]')
            # product_title = soup.find('div', {'class': 'shop-product-title'})
#            self.capacity = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
            #            self.capacity = (re.search('([0-9]+TB$)\w+', what_I_found.text)).group(1)
            # self.capacity = (re.search(r'\d+(?=TB)', what_I_found.text)).group(1)
            # self.capacity = re.findall('([0-9]+)\w+', self.capacity)
            self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
            # strip out the TB from the 12TB so that it's just a string of an integer
            self.capacity = (re.search(r'\d+', what_I_found.text)).group()
        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            self.capacity = "0TB"
            # print(e)

        return self.capacity


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

    def check_if_item_in_stock(self,driver):
        print(driver)
        try:
            # page_source.find_element(By.XPATH, '//button[text()="Add to Cart"]')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to cart"]')))
            driver.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page")
            print("Item is for NOT sale currently")
            self.successfully_found_element = False
            # print(e)

        return self.in_stock
    def get_price_of_item(self,driver):
        try:
            #
            # '//button[normalize-space()="Add to Cart"]')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//li[@class="price-current"]')))
            what_I_found = driver.find_element(By.XPATH, '//li[@class="price-current"]')
            print("what_I_found")
            print(what_I_found.text)
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)
        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            # print(e)

        return self.price

    def get_capactity_of_item(self, driver):
        price = ""
        try:
            what_I_found = driver.find_element(By.XPATH, '//h1[@class="product-title"]')
            self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            self.capacity = "0TB"
            # print(e)

        # strip out the TB from the 12TB so that it's just a string of an integer
        self.capacity = (re.search(r'\d+', what_I_found.text)).group()

        return self.capacity

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

    def check_if_item_in_stock(self,driver):

        print(driver)
        try:
            # page_source.find_element(By.XPATH, '//button[text()="Add to cart"]')
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Add to cart"]')))
            driver.find_element(By.XPATH, '//button[normalize-space()="Add to cart"]')
            #https://www.geeksforgeeks.org/python-selenium-find-button-by-text/
            #Note: It is recommended to use normalize-space() method because it trim the left and right side spaces. It is possible that there can be spaces present at the start or at the end of the target text.

            print("reached here")
            self.in_stock = True
        except Exception as e:
            print("Class is not available on the page")
            print("Item is for NOT sale currently")
            self.successfully_found_element = False
            # print(e)

        return self.in_stock

    def get_price_of_item(self,driver):

        try:
            what_I_found = driver.find_element(By.XPATH, '//span[@itemprop="price"]')
            self.price = (re.search('\$(\d+,?\d*\.\d+)', what_I_found.text)).group(1)

        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            # print(e)

        return self.price

    def get_capactity_of_item(self, driver):
        price = ""
        try:
            what_I_found = driver.find_element(By.XPATH, '//h1[@class="b lh-copy dark-gray mt1 mb2 f6 f3-m"]')
            self.capacity = (re.search(r'\d+TB', what_I_found.text)).group()
        except Exception as e:
            print("Class is not available on the page Price")
            self.successfully_found_element = False
            self.capacity = "0TB"
            # print(e)

        # strip out the TB from the 12TB so that it's just a string of an integer
        self.capacity = (re.search(r'\d+', what_I_found.text)).group()

        return self.capacity