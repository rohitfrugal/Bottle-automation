import logging
import unittest

import allure
from ddt import ddt, data, unpack
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from executions.LoginExecutions.LoginMethod import LoginMethod
from executions.TrackOrder.TrackOrderMethods import TrackOrderMethods

@ddt
@allure.feature('Track Order')
@allure.title('Tracking Order Check')
class TestTrackOrder(unittest.TestCase, BaseClass):
    log = Utils.custom_logger(logLevel=logging.WARNING)
    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.LoginMethod = LoginMethod(self.driver)
        self.TrackOrder = TrackOrderMethods(self.driver)

    # Test Case
    @allure.title(f"Checking Input in Track Order")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/TrackOrder/TrackOrder.xlsx", "SearchItem"))
    @unpack
    def test_check_input(self, orderID, currentTitle):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.TrackOrder.InputOrderID(orderID), currentTitle,
                             msg="Verification Failed to mismatch title.")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e


    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e