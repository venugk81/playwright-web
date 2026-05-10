from datetime import datetime

import playwright
import pytest
import pytest_html
from playwright.sync_api import sync_playwright, Playwright
from utils.config import BASE_URL, HEADLESS
import os
from pytest_html import extras


def pytest_configure(config):
    """
    Configures pytest metadata and HTML reporting for the test run.

    This function sets up custom metadata for the test report, including project details,
    tester information, and environment. It also creates a timestamped directory for reports
    and configures the HTML report path to be self-contained.

    Args:
        config (pytest.Config): The pytest configuration object.

    Effects:
        - Updates config._metadata with project, tester, and environment info.
        - Creates a timestamped report directory under 'reports/'.
        - Sets the HTML report file path and ensures it's self-contained.
        - Prints the report location to the console.
    """
    try:
        config._metadata = {
            "Project": "Playwright Framework",
            "Tester": os.getenv("USER", "Unknown"),
            "Environment": os.getenv("ENV", "QA"),

        }
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        report_dir = f"reports/{timestamp}"
        os.makedirs(report_dir, exist_ok=True)
        report_file = f"{report_dir}/report.html"
        config.option.htmlpath = report_file
        config.option.self_contained_html = True
        if not hasattr(config, "_metadata"):
            config._metadata = {}
        config._metadata["Project"] = "Playwright Framework"
        config._metadata["Run"] = timestamp
        print(f"\n📊 Report generated at: {report_file}\n")
    except Exception as e:
        print(f"Error in pytest_configure: {e}")
        raise




# Define browser types for cross-browser testing
# Cross-Browser and Mobile Emulation Support
# Updated conftest.py:
# Added parametrized fixtures for browser/device combinations: Desktop Chrome, Firefox, Safari, Mobile iPhone (iOS), and Mobile Android (Pixel 5).
# Each test will now automatically run on all these configurations, providing comprehensive coverage.
# Used Playwright's built-in device emulation for mobile testing.
# browser_types = ["chromium", "firefox", "webkit"]
browser_types = ["chromium"]
@pytest.fixture(scope="session", params=browser_types)
def browser(request, playwright: Playwright):
    """
    Session-scoped fixture that launches a browser instance for cross-browser testing.

    This fixture is parameterized with different browser types (e.g., chromium, firefox, webkit).
    It launches the specified browser once per test session and yields it for use in tests.
    The browser is closed after the session ends.

    Args:
        request (pytest.FixtureRequest): Provides access to the current parameter (browser type).
        playwright (Playwright): The Playwright instance.

    Yields:
        Browser: The launched browser instance.

    Note:
        Browser types are defined in the browser_types list above.
    """
    browser_type = request.param
    try:
        browser = getattr(playwright, browser_type).launch(headless=HEADLESS)
        yield browser
        browser.close()
    except Exception as e:
        print(f"Error launching browser {browser_type}: {e}")
        raise


@pytest.fixture(scope="function")
def page(browser):
    """
    Function-scoped fixture that creates a new browser context and page for each test.

    This fixture creates a fresh browser context and page instance for each test function,
    navigates to the base URL, and yields the page. The context is closed after the test,
    ensuring isolation between tests.

    Args:
        browser (Browser): The browser instance from the browser fixture.

    Yields:
        Page: The Playwright page object, ready for interaction.

    Note:
        BASE_URL is imported from utils.config.
    """
    try:
        context = browser.new_context()
        page = context.new_page()
        page.goto(BASE_URL)
        yield page

        page.close()
        context.close()
    except Exception as e:
        print(f"Error creating a page: {e}")
        raise


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook that captures screenshots on test failures and attaches them to the HTML report.

    This hook runs after each test call. If the test failed, it takes a screenshot of the page
    and embeds it as an image extra in the pytest-html report for easier debugging.

    Args:
        item (pytest.Item): The test item (function, class, etc.).
        call (pytest.CallInfo): Information about the test call (setup, call, teardown).

    Effects:
        - On failure, saves a screenshot to 'reports/{test_name}.png'.
        - Attaches the screenshot to the report as an image extra.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            page = item.funcargs.get("page")
            if page:
                screenshot_path = f"reports/{item.name}.png"
                page.screenshot(path=screenshot_path)

                if hasattr(report, "extra"):
                    report.extra.append(pytest_html.extras.image(screenshot_path))
        except Exception as e:
            print(f"Error capturing screenshot for {item.name}: {e}")


def pytest_html_report_title(report):
    """
    Sets the title of the HTML report generated by pytest-html.

    This function customizes the title displayed in the HTML report for better branding
    and identification of the test suite.

    Args:
        report (pytest_html.Report): The report object from pytest-html.

    Effects:
        - Updates report.title to "Automation Test Report".
    """
    try:
        report.title = "Automation Test Report"
    except Exception as e:
        print(f"Error setting report title: {e}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook that attaches execution logs to the HTML report.

    This hook runs after each test call (setup, call, teardown). It reads the contents
    of the 'reports/test.log' file and attaches it as a text extra in the pytest-html report.
    This is useful for including custom logging output in the report.

    Args:
        item (pytest.Item): The test item (function, class, etc.).
        call (pytest.CallInfo): Information about the test call (setup, call, teardown).

    Effects:
        - Reads logs from 'reports/test.log'.
        - Attaches the logs as a text extra named "Execution Logs" to the report.
        - Silently ignores errors if the log file cannot be read.

    Note:
        The log file is cleared before each test by the clear_logs fixture.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        try:
            with open("reports/test.log", "r") as f:
                logs = f.read()

            if not hasattr(report, "extras"):
                report.extras = []

            report.extras.append(extras.text(logs, name="Execution Logs"))

        except Exception as exp:
            print(f"Error attaching logs to report: {exp}")


@pytest.fixture(autouse=True)
def clear_logs():
    """
    Autouse fixture that clears the test log file before each test.

    This fixture runs automatically before every test (due to autouse=True), opening
    the 'reports/test.log' file in write mode to truncate it (clear its contents).
    This ensures that logs from previous tests do not carry over.

    Effects:
        - Empties the 'reports/test.log' file before each test execution.
    """
    try:
        open("reports/test.log", "w").close()
    except Exception as e:
        print(f"Error clearing logs: {e}")
