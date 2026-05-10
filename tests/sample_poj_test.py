class Practice:

    def __init__(self, page):
        self.page = page

    def practice_ui_operations(self, data):
        """
        UI Operations using Playwright
        """

        print("Executing Test Data:", data)

        self.page.goto("https://example.com")

        # Example
        # self.page.fill("#username", data["username"])