import pytest
from pages.google_page import GooglePage
from pages.rediff_register_page import RediffRegisterPage
from utils.FileUtils import get_excel_data
from utils.csv_reader import read_csv

test_data = get_excel_data("employee_data", "E001", "Employee")
@pytest.mark.parametrize("map_data", test_data )
def test_google_search(page, map_data):
    red = RediffRegisterPage(page)
    print(map_data)
    red.register2(map_data)




