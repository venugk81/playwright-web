from pages.base_page import BasePage

class GooglePage(BasePage):
    SEARCH_BOX = "textarea[name='q']"
    SEARCH_RESULTS = "h3"

    def search(self, text):
        self.fill(self.SEARCH_BOX, text)
        self.page.keyboard.press("Enter")

    def get_results(self):
        self.page.wait_for_selector(self.SEARCH_RESULTS, timeout=10000)
        return self.page.locator(self.SEARCH_RESULTS).all_inner_texts()
