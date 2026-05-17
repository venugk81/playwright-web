
import pytest
import allure
from pages.PracticePage import  PracticePage

from utils.FileUtils import get_csv_data_zero
from utils.result_manager import ResultManager


# test_data3 = get_csv_data_zero("practice_data", "Test1")

# @pytest.mark.parametrize("map_data3", test_data3)
# def test_practice(page, map_data3):
#     print("map data: ", map_data3)
#     red = Practice(page)
#     red.practice_ui_operations(map_data3)



@allure.feature("Rediff Registration")
class TestPracticeClass:
    test_data3 = get_csv_data_zero("sample_data", "Test_1")
    @pytest.mark.parametrize("map_data3", test_data3)
    def test_registration_method(self, page, map_data3):
        with allure.step(f"Read Test data for the test: {map_data3.get('EmailID')}"):
            print("Get data from CSV using parameterization: ", map_data3)

        red = PracticePage(page)
        with allure.step("Register new user profile: "):
            red.practice_ui_operations(map_data3)
            print("Registration successful: ", map_data3.get("EmailID"))

        ResultManager.attach_screenshot1(
            page,
            map_data3,
            "Results"
        )

# To run the script from cmd line: pytest -s tests/Testpractice01.py
# -s shows print() statements in console. without -s, pytest captures output.
# run specific test class: pytest -s test_user.py::TestUser

# pytest tests/test_rediff_registration.py --alluredir=reports/allure-results
# pytest -v tests/ui_tests/test_rediff_registration.py --alluredir=reports/allure-results
#       For Parallel Execution:
# pytest -v -n 3tests/ui_tests/test_rediff_registration.py --alluredir=reports/allure-results
# allure serve reports/allure-results