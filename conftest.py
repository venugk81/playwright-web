from datetime import datetime

import playwright
import pytest
import pytest_html
from playwright.sync_api import sync_playwright, Playwright
from utils.config import BASE_URL, HEADLESS
import os
from pytest_html import extras


# def pytest_configure(config):
#     os.makedirs("reports", exist_ok=True)
#     # config._metadata = {
#     #     "Project": "Playwright Framework",
#     #     "Module": "Google Search",
#     #     "Tester": "Venu",
#     #     "Env": "QA",
#     # }
#     config._metadata = {
#         "Project": "Playwright Framework",
#         "Tester": os.getenv("USER", "Unknown"),
#         "Environment": os.getenv("ENV", "QA"),
#     }
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     report_file = f"reports/report_{timestamp}.html"
#     print(f"\n📊 HTML Report: {report_file}\n")
#     # Inject html report path dynamically
#     config.option.htmlpath = report_file
#     config.option.self_contained_html = True
#     # Optional metadata
#     if not hasattr(config, "_metadata"):
#         config._metadata = {}
#     config._metadata["Project"] = "Playwright Framework"
#     config._metadata["Execution Time"] = timestamp


def pytest_configure(config):
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


@pytest.fixture(scope="function")
def page(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"reports/{item.name}.png"
            page.screenshot(path=screenshot_path)

            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(screenshot_path))


def pytest_html_report_title(report):
    report.title = "Automation Test Report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        try:
            with open("reports/test.log", "r") as f:
                logs = f.read()

            if not hasattr(report, "extras"):
                report.extras = []

            report.extras.append(extras.text(logs, name="Execution Logs"))

        except Exception:
            pass


@pytest.fixture(autouse=True)
def clear_logs():
    open("reports/test.log", "w").close()
