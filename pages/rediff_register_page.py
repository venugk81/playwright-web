from pages.base_page import BasePage

class RediffRegisterPage(BasePage):
    FULL_NAME = "Enter your full name"
    EMAIL_ID = "Enter Rediffmail ID"
    PASSWORD = "Enter password"
    RENTER_PASSWORD = "Retype password"
    DOB_DAY = 'select[name^="DOB_Day"]'
    DOB_MONTH = 'select[name^="DOB_Month"]'
    DOB_YEAR = 'select[name^="DOB_Year"]'
    GENDER = '[name^="gender"][value="f"]'
    COUNTRY = "[id='country']"
    RECOVERY_EMAIL = "Enter recovery email"
    MOBILE = "[id='mobno']"

    def register(self, data):
        """
        Register user with provided data dictionary.
        
        Args:
            data (dict): Dictionary containing registration fields like full_name, email, password, etc.
        
        Raises:
            Exception: Logs and reports any element interaction errors.
        """
        try:
            self.logger.info(f"Registering {data}")
            self.page.get_by_placeholder(self.FULL_NAME).fill(data.get("full_name", "Venu Gopal"))
            self.page.get_by_placeholder(self.EMAIL_ID, exact=False).fill(data.get("email", "gasdf@asdf.com"))
            self.page.get_by_placeholder(self.PASSWORD, exact=False).fill(data.get("password", "hagsdfkjahsdgf$"))
            self.page.get_by_placeholder(self.RENTER_PASSWORD, exact=False).fill(data.get("password", "hagsdfkjahsdgf$"))
            self.page.locator(self.DOB_DAY).select_option(data.get("dob_day", "07"))
            self.page.locator(self.DOB_MONTH).select_option(data.get("dob_month", "JUN"))
            self.page.locator(self.DOB_YEAR).select_option(data.get("dob_year", "1986"))
            self.page.locator(self.GENDER).check()
            self.page.locator(self.COUNTRY).select_option(data.get("country", "Australia"))
            self.page.get_by_placeholder(self.RECOVERY_EMAIL).fill(data.get("recovery_email", "kjadsf@gmail.com"))
            self.page.locator(self.MOBILE).fill(str(data.get("mobile", "234234")))
            self.logger.info("Registration completed successfully")
        except Exception as e:
            self.logger.error(f"Error during registration: {e}")
            print(f"Exception in register method: {e}")
            raise

    def register2(self, data):
        """
        Register user with hardcoded test data.
        
        Args:
            data (dict): Data parameter (not used, hardcoded values are used instead).
        
        Raises:
            Exception: Logs and reports any element interaction errors.
        """
        try:
            self.logger.info(f"Registering with hardcoded data")
            self.page.get_by_placeholder(self.FULL_NAME).fill("Venu Gopal")
            self.page.get_by_placeholder(self.EMAIL_ID, exact=False).fill("gasdf@asdf.com")
            self.page.get_by_placeholder(self.PASSWORD, exact=False).fill("hagsdfkjahsdgf$")
            self.page.get_by_placeholder(self.RENTER_PASSWORD, exact=False).fill("password")
            self.page.locator(self.DOB_DAY).select_option("07")
            self.page.locator(self.DOB_MONTH).select_option("JUN")
            self.page.locator(self.DOB_YEAR).select_option("1986")
            self.page.locator(self.GENDER).check()
            self.page.locator(self.COUNTRY).select_option("Australia")
            self.page.get_by_placeholder(self.RECOVERY_EMAIL).fill("kjadsf@gmail.com")
            self.page.locator(self.MOBILE).fill(str("234234"))
            self.logger.info("Registration with hardcoded data completed successfully")
        except Exception as e:
            self.logger.error(f"Error during registration2: {e}")
            print(f"Exception in register2 method: {e}")
            raise

    def register3(self, map_data):
        """
        Register using data from Excel file with direct column mapping.
        
        Args:
            map_data (dict): Dictionary with columns: EmailID, Password, DOB_Day, DOB_Month, DOB_Year, 
                           Gender, Country, Recovery_Email, Mobile, Name.
        
        Raises:
            Exception: Logs and reports any element interaction errors.
        """
        try:
            self.logger.info(f"Registering with Excel data: {map_data}")
            self.page.get_by_placeholder(self.FULL_NAME).fill(map_data.get("Name", "Test User"))
            self.page.get_by_placeholder(self.EMAIL_ID, exact=False).fill(map_data.get("EmailID", "test@rediffmail.com"))
            password = map_data.get("Password", "TestPass123!")
            self.page.get_by_placeholder(self.PASSWORD, exact=False).fill(password)
            self.page.get_by_placeholder(self.RENTER_PASSWORD, exact=False).fill(password)
            self.page.locator(self.DOB_DAY).select_option("08")
            self.page.locator(self.DOB_MONTH).select_option("JUN")
            self.page.locator(self.DOB_YEAR).select_option(str(map_data.get("DOB_Year")))
            self.page.locator(self.GENDER).check()
            self.page.locator(self.COUNTRY).select_option(map_data.get("Country", "India"))
            self.page.get_by_placeholder(self.RECOVERY_EMAIL).fill(map_data.get("Recovery_Email", "recovery@example.com"))
            self.page.locator(self.MOBILE).fill(str(map_data.get("Mobile", "1234567890")))
            self.logger.info("Registration with Excel data completed successfully")
        except Exception as e:
            self.logger.error(f"Error during registration3 with data {map_data}: {e}")
            print(f"Exception in register3 method: {e}")
            raise

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
