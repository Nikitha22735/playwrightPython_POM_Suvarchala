
# from operator import call

import pytest
import allure


@pytest.fixture()
def naviagetToBrowser(page):
    page.goto("https://www.amazon.in/")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        # Test has failed, capture screenshot
        screenshot_path = f"screenshots/{item.name}.png"
        item.funcargs['page'].screenshot(path=screenshot_path)
        # Attach the screenshot to the Allure report       
        allure.attach.file(screenshot_path, name="screenshot", attachment_type=allure.attachment_type.PNG)