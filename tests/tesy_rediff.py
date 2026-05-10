import pytest

from pages.rediff_register_page import RediffRegisterPage
from utils.FileUtils import get_excel_data, get_csv_data, get_csv_data_zero


test_data = get_excel_data("employee_data", "E001", "Employee")


@pytest.mark.parametrize("map_data", test_data)
def test_google_search(page, map_data):
    red = RediffRegisterPage(page)
    print(map_data)
    red.register2(map_data)


test_data2 = get_csv_data("sample_data", "Test_1")


@pytest.mark.parametrize("map_data2", test_data2)
def test_csv_data1(page, map_data2):
    print(map_data2)
    red = RediffRegisterPage(page)
    red.register3(map_data2)


test_data3 = get_csv_data_zero("products", "TC043")


@pytest.mark.parametrize("map_data3", test_data3)
def test_csv_data2(page, map_data3):
    print(map_data3)
    red = RediffRegisterPage(page)
    red.print_map_data(map_data3)
