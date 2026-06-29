from pages.homePage import home

from playwright.sync_api import sync_playwright, expect

def test_validateSearchResults(page):
    page.goto("https://www.amazon.in/")
    homePageObj = home(page)
    homePageObj.enterProductInSearchBox("iphone")
    homePageObj.clickOnSearchBtn()
    expect(page).to_have_title("Amazon.in : iphone")