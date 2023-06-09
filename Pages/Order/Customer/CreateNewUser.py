import time
import logging

from Utilities.utils import Utils
from selenium.webdriver import Keys
from Pages.Order.OrderPage import OrderPage


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as Exceptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException




class CreateNewUser(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Order_module", logLevel=logging.WARNING)

    # Locators
    # For new user.
    InputName = (By.ID, 'name')
    InputEmail = (By.ID, 'email')
    InputDob = (By.ID, 'dob')  # Format - 2022-12-12
    InputAddress = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/input')
    SuggestedAddress = (By.XPATH, '/html/body/div[5]')
    SubmitUser = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div/div/div/div[6]/div/div/div/div/div/button/span')

    # Verify Create User
    PageHeader = (By.XPATH, '//*[@id="root"]/section/main/div/div/h2')

    # Methods

    # Filling user details New customer form.
    def input_name(self, name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.InputName)).send_keys(name)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to input the name")

    def input_email(self, email):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.InputEmail)).send_keys(email)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to input email")

    def input_dob(self, dob):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.InputDob)).send_keys(dob)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to input DOB")

    def input_address(self, address):
        try:
            user_address = self.wait.until(EC.visibility_of_element_located(self.InputAddress))
            user_address.send_keys(address)
            time.sleep(1)
            user_address.send_keys(Keys.SPACE)
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pac-container")))
            time.sleep(1)
            user_address.send_keys(Keys.DOWN)
            time.sleep(1)
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pac-item"))).click()
            time.sleep(1)
        except (TimeoutException, NoSuchElementException, Exceptions) as e:
            self.log.error(f"Failed to input address. {str(e)}")

    def submit_new_user(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.SubmitUser)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find Submit button : {str(e)}")
    def verify_Create_user(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PageHeader)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the verification Text : {str(e)}")
