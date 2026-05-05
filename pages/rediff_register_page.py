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
        self.logger.info(f"Registering {data}")
        self.page.get_by_placeholder(self.FULL_NAME).fill(data.get("full_name", "Venu Gopal"))
        # self.fill(self.FULL_NAME, data.get("full_name", "Venu Gopal"))
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

    def register2(self, data):
        self.logger.info(f"Registering {data}")
        self.page.get_by_placeholder(self.FULL_NAME).fill("Venu Gopal")

        self.page.get_by_placeholder(self.EMAIL_ID, exact=False).fill("gasdf@asdf.com")
        self.page.get_by_placeholder(self.PASSWORD, exact=False).fill("hagsdfkjahsdgf$")
        self.page.get_by_placeholder(self.RENTER_PASSWORD, exact=False).fill("password", "hagsdfkjahsdgf$")
        self.page.locator(self.DOB_DAY).select_option("07")
        self.page.locator(self.DOB_MONTH).select_option("JUN")
        self.page.locator(self.DOB_YEAR).select_option("1986")
        self.page.locator(self.GENDER).check()
        self.page.locator(self.COUNTRY).select_option("Australia")
        self.page.get_by_placeholder(self.RECOVERY_EMAIL).fill("kjadsf@gmail.com")
        self.page.locator(self.MOBILE).fill(str("234234"))