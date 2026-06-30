
import pytest


@pytest.fixture()
def naviagetToBrowser(page):
    page.goto("https://www.amazon.in/")