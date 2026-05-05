from utils.logger import get_logger


class BasePage:
    def __init__(self, page):
        self.logger = get_logger()
        self.page = page

    def navigate(self, url):
        self.logger.info(f"Navigating to url: {url}")
        self.page.goto(url)

    def click(self, locator):
        self.logger.info(f"Clicking on element: {locator}")
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.logger.info(f"Filling element: {locator}")
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        self.logger.info(f"Getting element text: {locator}")
        return self.page.locator(locator).inner_text()
