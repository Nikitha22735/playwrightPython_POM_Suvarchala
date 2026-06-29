from playwright.sync_api import sync_playwright, expect
from pages.homePage import home

def test_ValidateTheUIElementsOnHomeScreen(page):
   page.goto("https://www.amazon.in/")
   expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
   homePageObj = home(page)
   homePageObj.validateTheVisibityOfSearchBox()
   expect(page.locator("#nav-hamburger-menu")).to_be_visible()
   expect(page.get_by_text("Account & Lists")).to_be_visible()
