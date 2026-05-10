# test_sample.py

import pytest


# SESSION SCOPE
@pytest.fixture(scope="session")
def server():
    print("\n[SETUP] session Start Server")
    yield "Server Started"
    print("\n[TEARDOWN] session Stop Server")


# MODULE SCOPE
@pytest.fixture(scope="module")
def database(server):       #database is refering to server fixture.
    print("\n[SETUP] module Connect Database")
    yield "DB Connected"
    print("\n[TEARDOWN] module Disconnect Database")


# CLASS SCOPE
@pytest.fixture(scope="class")
def login(database):    #login is referring to database fixture.
    print("\n[SETUP] class Login User")
    yield "User Logged In"
    print("\n[TEARDOWN] class Logout User")


# FUNCTION SCOPE
@pytest.fixture(scope="function")
def test_data():
    print("\n[SETUP] function  Create Test Data")
    yield {"name": "Venu"}
    print("\n[TEARDOWN] function Delete Test Data")


# TEST CLASS
class TestExample:

    #login is a class level fixture, so it will run once for all tests in this class
    #test_data is a function level fixture, so it will run before each test method
    def test_one(self, test_data):
        print("Running Test One---------1")
        print(test_data)

    def test_two(self, login):
        print("Running Test Two---------2")
        # print(test_data)

    def test_three(self, login, test_data):
        print("Running Test three---------3")
        print(test_data)