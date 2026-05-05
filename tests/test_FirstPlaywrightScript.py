import time

import playwright
import pytest


# from playwright.sync_api import sync_playwright

def test_fixture(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://register.rediff.com/register/register.php?FormName=user_details")
    # page.get_by_title("Search").fill("testing")
    # page.get_by_title("Search").press("Enter")
    page.get_by_placeholder("Enter your full name").fill("Venu Gopal")
    page.get_by_placeholder("Enter Rediffmail ID", exact=False).fill("gopivenu9kjasdfkasdf")
    page.get_by_placeholder("Enter password", exact=False).fill("hagsdfkjahsdgf$")
    page.get_by_placeholder("Retype password", exact=False).fill("hagsdfkjahsdgf$")
    page.locator('select[name^="DOB_Day"]').select_option("07")
    page.locator('select[name^="DOB_Month"]').select_option("JUN")
    page.locator('select[name^="DOB_Year"]').select_option("1986")
    page.locator('[name^="gender"][value="f"]').check()
    page.locator("[id='country']").select_option("Australia")
    page.get_by_placeholder("Enter recovery email").fill("kjadsf@gmail.com")
    # page.locator('[name^="chk"]').check()
    page.locator('[id="mobno"]').fill("7773884")
    time.sleep(2)
    page.close()
    browser.close()

