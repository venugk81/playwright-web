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

    @staticmethod
    def attach_text1(name, map_data, content):
        allure.attach(
            content,
            name=name,
            attachment_type=allure.attachment_type.TEXT,
            extension=map_data
        )

    @staticmethod
    def attach_screenshot1(page, map_data, name):
        print("Reporting fro attach screenshot method..")
        allure.attach(
            page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
            extension=map_data
        )