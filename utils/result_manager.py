import allure


class ResultManager:

    @staticmethod
    def attach_text(name, content):

        allure.attach(
            content,
            name=name,
            attachment_type=allure.attachment_type.TEXT
        )

    @staticmethod
    def attach_screenshot(page, name):

        allure.attach(
            page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )