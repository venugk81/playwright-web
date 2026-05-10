# test_sample.py

import pytest


# SESSION SCOPE
@pytest.fixture(scope="session")
def server():
    print("\n[SETUP] Start Server")
    yield "Server Started"
    print("\n[TEARDOWN] Stop Server")


# MODULE SCOPE
@pytest.fixture(scope="module")
def database(server):
    print("\n[SETUP] Connect Database")
    yield "DB Connected"
    print("\n[TEARDOWN] Disconnect Database")


# CLASS SCOPE
@pytest.fixture(scope="class")
def login(database):
    print("\n[SETUP] Login User")
    yield "User Logged In"
    print("\n[TEARDOWN] Logout User")


# FUNCTION SCOPE
@pytest.fixture(scope="function")
def test_data():
    print("\n[SETUP] Create Test Data")
    yield {"name": "Venu"}
    print("\n[TEARDOWN] Delete Test Data")


# TEST CLASS
class TestExample:

    def test_one(self, login, test_data):
        print("Running Test One")
        print(test_data)

    def test_two(self, login, test_data):
        print("Running Test Two")
        print(test_data)