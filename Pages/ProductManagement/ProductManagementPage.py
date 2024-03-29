import logging
import time

from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException


class ProductManagementPage():
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.actionChain = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Product_management", logLevel=logging.WARNING)

    # Methods
    PRODUCT_TAB = (By.ID, "ProductManagementMenu")
    HEADER_TEXT = (By.XPATH, "//h1[@class='ant-typography']")

    # Operations
    ADD_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary add__button']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary']")

    # Upload Image
    UPLOAD_IMG = (By.XPATH, "//input[@type='file']")
    OK_BTN = (By.XPATH, "//button[@class= 'ant-btn ant-btn-primary']/span[contains(text(), 'OK')]")

    # Add Product Page
    PRODUCT_NAME = (By.XPATH, "//input[@id='basic_name']")
    SLUG = (By.XPATH, "//input[@id='basic_slug']")

    CATEGORY = (By.XPATH, "//input[@id='basic_category']")
    ALL_ITEM_SELECTOR = (By.XPATH, "(//div[@class='rc-virtual-list-holder-inner'])[1]/div")
    VISIBLE_ELEMENTS = (By.XPATH, "(//div[contains(@class,'ant-select-item ant-select-item-option')])")

    GENDER = (By.XPATH, "(//div[@class='ant-select-selector'])[2]/span")
    RANKING_level = (By.XPATH, "(//div[@class='ant-select-selector'])[3]/span")
    VISIBLE_RANKS_ELEMENT = (By.XPATH,"(//div[@class='rc-virtual-list-holder-inner'])[3]//div[contains(@class, 'ant-select-item ant-select-item-option')]")
    ALL_VISIBLE_RANK_LOCATOR = (By.XPATH, "(//div[@class='rc-virtual-list-holder-inner'])[3]/div")
    TAGS = (By.XPATH, "//input[@id='basic_tags']")
    HARDWARE = (By.XPATH, "//input[@id='basic_hardware']")
    LINING = (By.XPATH, "//input[@id='basic_lining']")
    POLYFILL = (By.XPATH, "(//div[@class='ant-switch-handle'])[1]")
    RIB = (By.XPATH, "(//div[@class='ant-switch-handle'])[2]")
    DESCRIPTION = (By.XPATH, "//textarea[@id='basic_description']")

    # Confirmation Msg
    ADDED_CONFIRM_MSG = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-success']/span")  # Product updated successfully
    ERROR_MSG = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-error']/span")

    # Add Leather Profile
    ADD_LEATHER_PROFILE = (By.XPATH, "(//div[@class='ant-tabs-tab-btn'])[2]")

    ADD_NEW_LEATHER = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-default']")
    SELECT_LEATHER = (By.XPATH, "//div[@class='ant-collapse-item leather__group__panel']")
    SELECT_LEATHER_CATEGORY = (By.XPATH, "(//span[@class='ant-select-selection-search'])[4]")

    # Duplication Leather Profile
    DUPLICATE_BUTTON = (By.XPATH, "(//button[@class='ant-btn ant-btn-round ant-btn-text'])[1]")
    DUPLICATE_SELECTOR = (By.XPATH, "//div[@class='ant-modal-body']/div/div[@class='ant-select-selector']")
    ALL_DUPLICATE_SELECTOR = (By.XPATH, "(//div[@class='rc-virtual-list-holder-inner'])[5]/div")
    ALL_DUPLICATE_VISIBLE_SELECTOR = (By.XPATH, "(//div[@class='rc-virtual-list-holder-inner'])[5]//div[contains(@class,'ant-select-item ant-select-item-option')]")

    UPDATE = (By.XPATH, "(//button[@class='ant-btn ant-btn-round ant-btn-primary'])[2]")
    SUBMIT_DUPLICATE = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")


    # Editing Product
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search']")
    PRODUCT_DIV = (By.XPATH, "//div[@class='ant-card ant-card-bordered ant-card-hoverable product__item__card']/div[@class='ant-card-body']")
    EDIT_BUTTON = (By.XPATH, "//div[@class='hoverable__action']/div/div[@class='ant-space-item'][2]/span")
    VIEW_BUTTON = (By.XPATH, "//div[@class='hoverable__action']/div/div[@class='ant-space-item'][1]/span")


    # Secondary Image
    SECONDARY_IMAGE_TAB = (By.XPATH, "//div[@class='ant-tabs-tab']/div[contains(text(), 'Secondary Images')]")
    UPLOAD_MORE_BTN = (By.XPATH, "(//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active'])/div/div/div[3]/div/div")
    INPUT_SECONDARY_IMAGES = (By.XPATH, "//div[@class='ant-upload ant-upload-drag common-s3-upload--container  ']/span/input[@type='file']")
    UPDATE_PRIMARY_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # Confirm Image upload -MSG
    IMAGE_UPDATED_SUCCESSFULLY = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-success']")


    # Check
    GET_NAME = (By.XPATH, "(//h1[@class='ant-typography'])[2]")
    GET_CATEGORY = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[1]")
    GET_TAG = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[2]")
    GET_HARDWARE = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[3]")
    GET_LINING = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[4]")
    GET_POLYFILL = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[5]")
    GET_RIB = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[6]")




    # ************** #
    # Helper Methods #
    # ************** #

    def HandleDropdown(self, dropDownLocator, value, VISIBLE_ELEMENTS, ALL_ITEM_SELECTOR):
        """
        :param dropDownLocator: Dropdown selector - click on Dropdown
        :param value: Selecting Value
        :param VISIBLE_ELEMENTS: First element of the list
        :param ALL_ITEM_SELECTOR: Div selector
        :return : If element is found click
        """
        # Setting up the flags
        itme_found = False

        # Click on the Dropdown
        print("finding the Category selector!")
        time.sleep(3)
        self.driver.find_element(*dropDownLocator).click()

        # Getting to all the elements
        ELEMENTS = self.wait.until(EC.visibility_of_element_located(VISIBLE_ELEMENTS))
        self.actionChain.move_to_element(ELEMENTS).perform()
        elements = self.driver.find_elements(*ALL_ITEM_SELECTOR)
        print(f"List retrieved length : {len(elements)}")

        # Repeat until you find a match
        while True:
            for element in elements:
                try:
                    if element.is_displayed():
                        if value == element.text:
                            print(f"found : {value}.")
                            element.click()
                            itme_found = True
                            break
                except StaleElementReferenceException:
                    print("This is for StaleElementReferenceException")
                    continue
            if itme_found:
                break
            try:
                self.actionChain.send_keys(Keys.ARROW_DOWN).perform()
                elements = self.driver.find_elements(*ALL_ITEM_SELECTOR)
            except NoSuchElementException:
                print("This is for NoSuchElementException")

                break
        if not itme_found:
            print(f"Item not Found {value}.")

    def search(self, search_item):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SEARCH_BAR)).send_keys(search_item)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find search bar locator : {str(e)}")

    def navigate(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TAB)).click()
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate Nav Item : {str(e)}")

    def get_headerText(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HEADER_TEXT)).text
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to fetch the title Text : {str(e)}")

    def clear(self, SELECTOR):
        try:
            self.wait.until(EC.visibility_of_element_located(SELECTOR)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.visibility_of_element_located(SELECTOR)).send_keys(Keys.BACKSPACE)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find  the Selector image locator : {str(e)} ")

    def scroll_up(self):
        self.driver.execute_script("window.scrollBy(0, -window.innerHeight);")

    # ******************* #
    # Product Basic input #
    # ******************* #

    def upload_img(self, imgPath):
        try:
            self.driver.find_element(*self.UPLOAD_IMG).send_keys(imgPath)
            return self.wait.until(EC.visibility_of_element_located(self.OK_BTN)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find upload image locator : {str(e)} ")

    def clik_on_add(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find the add item button : {str(e)}")

    def enter_product_name(self, name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME)).send_keys(name)
        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Product name input box : {str(e)}")

    def get_category(self, category_name):
        try:
            self.HandleDropdown(self.CATEGORY, category_name, self.VISIBLE_ELEMENTS, self.ALL_ITEM_SELECTOR)
        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Category selector : {str(e)}")

    def get_gender(self, gender):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GENDER)).click()
            gender_element = (
            By.XPATH, f"//div[contains(@class,'ant-select-item ant-select-item-option')][contains(@title,'{gender}')]")
            return self.wait.until(EC.visibility_of_element_located(gender_element)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate gender element : {str(e)}")

    def get_ranking(self, rank):
        try:
            self.HandleDropdown(self.RANKING_level, rank, self.VISIBLE_RANKS_ELEMENT, self.ALL_VISIBLE_RANK_LOCATOR)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Rank element : {str(e)}")

    def get_Tags(self, tags):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TAGS)).click()
            self.wait.until(EC.visibility_of_element_located(self.TAGS)).send_keys(tags)
            self.wait.until(EC.visibility_of_element_located(self.TAGS)).send_keys(Keys.ENTER)
            return self.wait.until(EC.visibility_of_element_located(self.TAGS)).send_keys(Keys.TAB)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Tag element : {str(e)}")

    def get_hardware(self, hardware):
        try:
            self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).click()
            self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(hardware)
            return self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(Keys.ENTER)
        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate hardware element : {str(e)}")

    def get_lining(self, lining):
        try:
            self.wait.until(EC.visibility_of_element_located(self.LINING)).click()
            self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(lining)
            return self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(Keys.ENTER)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate lining element : {str(e)}")

    def get_polyfill(self, polyfill_flag):
        try:
            if polyfill_flag:
                return self.wait.until(EC.visibility_of_element_located(self.POLYFILL)).click()
            else:
                self.actionChain.send_keys(Keys.TAB)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Polyfil element : {str(e)}")

    def get_rib(self, rib_flag):
        try:
            if rib_flag:
                return self.wait.until(EC.visibility_of_element_located(self.RIB)).click()
            else:
                self.actionChain.send_keys(Keys.TAB)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Rib element : {str(e)}")

    def enter_description(self, description):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.DESCRIPTION)).send_keys(description)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate description element to enter descriptions : {str(e)}")

    def enter_pattern_packages(self, sizes):
        try:
            # List of Selector and Size
            sizes = sizes.split(",")
            selectors = ["XXXS", "XXS", "XS", "S", "M", "ML", "L", "XL", "XXL", "XXXL"]
            for selector, size in zip(selectors, sizes):
                PACKAGE_SELECTOR = (By.XPATH, f"//input[@id='basic_pattern_package_{selector}']")
                self.wait.until(EC.visibility_of_element_located(PACKAGE_SELECTOR)).send_keys(size)

        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"{str(e)}")

    def submit_package(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate the Submit Button : {str(e)}")

    # ********************** #
    # Adding Leather Profile #
    # ********************** #

    def click_on_add_leather_profile(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ADD_LEATHER_PROFILE)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Add Leather Profile : {str(e)}")

    def click_on_add_leather(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ADD_NEW_LEATHER)).click()
        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find All Leather Button : {str(e)}")

    def click_on_select_leather(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SELECT_LEATHER)).click()
        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find All Leather Button : {str(e)}")

    def click_on_select_edit_leather(self):
        try:
            EDIT_LEATHER = (By.XPATH, "(//div[@class='ant-collapse-item leather__group__panel'])[2]")
            self.wait.until(EC.visibility_of_element_located(EDIT_LEATHER)).click()
        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find All Leather Button : {str(e)}")

    def get_leather_type(self, leatherType):
        try:
            self.HandleDropdown(self.SELECT_LEATHER_CATEGORY, leatherType, self.VISIBLE_ELEMENTS,  self.ALL_ITEM_SELECTOR)
        except (TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find Leather Type selector ")

    def get_Sizes(self, sizes, prices):
        try:
            counter = 1
            sizes = sizes.split(",")
            prices = prices.split(", ")
            print(f"All the available Size : {type(sizes)}")
            print(f"All the available Size : {sizes}")

            print(f"All the available Size : {type(prices)}")
            print(f"All the available Size : {prices}")

            for size, price in zip(sizes, prices):
                print(f"Selected size : {size}")

                SIZE_SELECTOR = (By.XPATH, f"((//div[@class='ant-select-selector'])[{7+counter}])")
                ALL_SIZE_SELECTOR = (By.XPATH, f"(//div[@class='rc-virtual-list-holder-inner'])[{1+counter}]/div")
                ALL_VISIBLE_SIZE_SELECTOR = (By.XPATH, f"((//div[@class='rc-virtual-list-holder-inner'])[{1+counter}]/div[contains(@class,'ant-select-item ant-select-item-option')])")
                ADD_SIZE = (By.XPATH, f"(//div[@class='ant-space ant-space-horizontal ant-space-align-center'])[{2+counter}]/div[2]")
                PRICE_INPUT = (By.XPATH, f"(//div[@class='ant-input-number-input-wrap'])[{counter}]/input")

                # Selecting Size
                self.HandleDropdown(SIZE_SELECTOR, size, ALL_VISIBLE_SIZE_SELECTOR, ALL_SIZE_SELECTOR)

                # Clearing Default Price
                self.clear(PRICE_INPUT)

                # Input New Price
                self.wait.until(EC.visibility_of_element_located(PRICE_INPUT)).send_keys(price)
                time.sleep(3)
                self.wait.until(EC.visibility_of_element_located(ADD_SIZE)).click()
                counter += 1

            SUBTRACT_BUTTON = (By.XPATH, f"(//div[@class='ant-space ant-space-horizontal ant-space-align-center'])[{2+counter}]/div[1]")
            self.wait.until(EC.visibility_of_element_located(SUBTRACT_BUTTON)).click()

        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find the Size selector {str(e)}")

    def click_update(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.UPDATE)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find Update Button : {str(e)}")

    def duplicate_Leather_profile(self, duplicate_leather):
        try:
            print(f"Duplicate-leather item : {duplicate_leather}")
            self.driver.find_element(*self.DUPLICATE_BUTTON).click()
            self.HandleDropdown(self.DUPLICATE_SELECTOR, duplicate_leather, self.ALL_DUPLICATE_SELECTOR, self.ALL_DUPLICATE_VISIBLE_SELECTOR)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Locate duplicate button : {str(e)}")

    def click_duplicate(self):
        try:
            self.driver.find_element(*self.SUBMIT_DUPLICATE).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find Duplicate Creation Button : {str(e)}")

    # *********************** #
    # Adding Secondary Images #
    # *********************** #

    def navigate_to_secondary_img(self):
        try:
            self.scroll_up()
            self.wait.until(EC.visibility_of_element_located(self.SECONDARY_IMAGE_TAB)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find Secondary Image Tab : {str(e)}")

    def click_upload_img(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.UPLOAD_MORE_BTN)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find Upload more Image : {str(e)}")

    def input_secondary_img(self, secondaryImg):
        try:
            self.driver.find_element(*self.INPUT_SECONDARY_IMAGES).send_keys(secondaryImg)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find Secondary Image Input box : {str(e)}")

    def submit_secondary_img(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.UPDATE_PRIMARY_BTN)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find Submit Button for Secondary Image : {str(e)}")

    def get_confirm_msg(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.IMAGE_UPDATED_SUCCESSFULLY)).text
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find confirmation message : {str(e)}")



    # TODO --- Continue This after creating the edit as it will add a lot of items in the list.

    # *********************** #
    # Editing Leather Profile #
    # *********************** #

    def click_on_edit(self):
        try:
            PRODUCT = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_DIV))
            self.actionChain.move_to_element(PRODUCT).perform()
            self.wait.until(EC.visibility_of_element_located(self.EDIT_BUTTON)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find edit button for the Product : {str(e)}")



    # ********************** #
    # Check Synchronization  #
    # ********************** #

    def click_on_view(self):
        try:
            PRODUCT = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_DIV))
            self.actionChain.move_to_element(PRODUCT).perform()
            self.wait.until(EC.visibility_of_element_located(self.VIEW_BUTTON)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find edit button for the Product : {str(e)}")

    def view_name(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GET_NAME)).text()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find Name field : {str(e)}")

    def view_category(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GET_CATEGORY)).text()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find category field : {str(e)}")

    def view_tag(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GET_TAG)).text()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find Tag field : {str(e)}")

    def view_hardware(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GET_HARDWARE)).text()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find Hardware field : {str(e)}")

    def view_lining(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.GET_LINING)).text()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find Lining field : {str(e)}")

    def view_polyfill(self):
        try:
            if self.wait.until(EC.visibility_of_element_located(self.GET_POLYFILL)).text() == "Yes":
                return "TRUE"
            else:
                return "FALSE"
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find Polyfill field : {str(e)}")

    def view_rib(self):
        try:
            if self.wait.until(EC.visibility_of_element_located(self.GET_RIB)).text() == "Yes":
                return "TRUE"
            else:
                return "FALSE"
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to Find rib field : {str(e)}")
