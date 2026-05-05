import time

import playwright
import pytest
from playwright.sync_api import Playwright

from utils.FileUtils import get_excel_data


# from playwright.sync_api import sync_playwright
@pytest.mark.parametrize("map_data", get_excel_data("employee_data", "E001", "Employee"))
def test_fixture(playwright: Playwright, map_data):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://register.rediff.com/register/register.php?FormName=user_details")
    # page.get_by_title("Search").fill("testing")
    # page.get_by_title("Search").press("Enter")
    # ID, Name, Department, Gender, Mobile
    page.get_by_placeholder("Enter your full name").fill("Venu Gopal")
    page.get_by_placeholder("Enter Rediffmail ID", exact=False).fill(f"{map_data['Name']}")
    page.get_by_placeholder("Enter password", exact=False).fill("hagsdfkjahsdgf$")
    page.get_by_placeholder("Retype password", exact=False).fill("hagsdfkjahsdgf$")
    page.locator('select[name^="DOB_Day"]').select_option("07")
    page.locator('select[name^="DOB_Month"]').select_option("JUN")
    page.locator('select[name^="DOB_Year"]').select_option("1986")
    page.locator('[name^="gender"][value="f"]').check()
    page.locator("[id='country']").select_option("Australia")
    page.get_by_placeholder("Enter recovery email").fill("kjadsf@gmail.com")
    # page.locator('[name^="chk"]').check()
    page.locator('[id="mobno"]').fill(f"{map_data['Mobile']}")
    # time.sleep(2)
    page.close()
    browser.close()

import pandas as pd
# import seaborn as sbn
# s = sbn.load_dataset("titanic")
# print(s.head())