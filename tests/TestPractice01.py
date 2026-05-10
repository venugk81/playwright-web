import allure
import pytest

from pages.PracticePage import  PracticePage

from utils.FileUtils import get_csv_data_zero

# test_data3 = get_csv_data_zero("practice_data", "Test1")
#
#
# @pytest.mark.parametrize("map_data3", test_data3)
# def test_practice(page, map_data3):
#     print("map data: ", map_data3)
#     red = Practice(page)
#     red.practice_ui_operations(map_data3)




class TestPractice:
    test_data3 = get_csv_data_zero("sample_data", "Test_1")
    @pytest.mark.parametrize("map_data3", test_data3)
    def test_practice(self, page, map_data3):
        print(map_data3)
        red = PracticePage(page)
        red.practice_ui_operations(map_data3)

# To run the script from cmd line: pytest -s tests/Testpractice01.py
# -s shows print() statements in console. without -s, pytest captures output.
# run specific test class: pytest -s test_user.py::TestUser