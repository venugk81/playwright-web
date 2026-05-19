import time

import pytest

from pages.base_page import BasePage


class PracticePage(BasePage):
    FULL_NAME = "[placeholder='Enter your full name']"
    EMAIL_ID = "input[placeholder='Enter Rediffmail ID']"
    PASSWORD = "[placeholder='Enter password']"
    RENTER_PASSWORD = "[placeholder='Retype password']"
    DOB_DAY = 'select[name^="DOB_Day"]'
    DOB_MONTH = 'select[name^="DOB_Month"]'
    DOB_YEAR = 'select[name^="DOB_Year"]'
    GENDER = '[name^="gender"]'
    COUNTRY = "[id='country']"
    RECOVERY_EMAIL = "[placeholder='Enter recovery email']"
    MOBILE = "[id='mobno']"



    def practice_ui_operations(self, map_data):
        print("map data passed successfully to run the test method: ", map_data)
        try:
            # Navigate to the practice page
            self.logger.info(f"\nRegistering with Excel data: {map_data}")
            self.fill(self.FULL_NAME, map_data.get("Testname"))
            self.fill(self.EMAIL_ID, map_data.get("EmailID"))
            self.fill(self.PASSWORD, map_data.get("Password"))
            self.fill(self.RENTER_PASSWORD, map_data.get("confirmPassword"))
            self.select_dropdown_option(self.DOB_DAY, map_data.get("DOB_Day"))
            self.select_dropdown_option(self.DOB_MONTH, map_data.get("DOB_Month"))
            self.select_dropdown_option(self.DOB_YEAR, map_data.get("DOB_Year"))
            # self.select_radio_by_text(self.GENDER, map_data.get("GENDER", "M"))
            if map_data.get("EmailID") == "xatiw@example.com":
                map_data['Status']='Fail'
                print("Simulated failure for email ID: ", map_data.get("EmailID"))
                print("map_data: ", map_data)
                pytest.fail ("Script failure - intentional failure")
            else:
                map_data['Status']='Pass'
            print("Script passed and map_data is updated: ", map_data)

        #     self.logger.info("Registration with Excel data completed successfully")
        except Exception as e:
            map_data['Status'] = 'Fail'
        #     self.logger.error(f"Error during registration3 with data {map_data}: {e}")
            print(f"Exception in register3 method: {e}. map_data: {map_data}")
            raise e

    def print_map_data(self, map_data):
        """
        Prints all key-value pairs from the provided data dictionary.

        Args:
            map_data (dict): Dictionary with test data to print.

        Raises:
            Exception: Logs and reports any iteration or printing errors.
        """
        try:
            self.logger.info(f"Printing map data: {map_data}")
            for key, value in map_data.items():
                print(f"{key}: {value}")
            self.logger.info("Map data printed successfully")
        except Exception as e:
            self.logger.error(f"Error printing map data: {e}")
            print(f"Exception in print_map_data method: {e}")
            raise
