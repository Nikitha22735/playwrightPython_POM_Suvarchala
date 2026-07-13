import allure
from playwright.sync_api import sync_playwright, expect
import pytest
from pages.homePage import home

# @pytest.mark.home
# @pytest.mark.regression
@pytest.mark.smoke
def test_ValidateTheUIElementsOnHomeScreen(page):
   page.goto("https://www.amazon.in/")
   expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
   homePageObj = home(page)
   homePageObj.validateTheVisibityOfSearchBox()
   @allure.step("Validate the visibility of hamburger menu")
   def validateTheVisibilityOfHamburgerMenu():
      expect(page.locator("#nav-hamburger-menu")).to_be_visible()
   # expect(page.locator("#nav-hamburger-menu")).to_be_visible()
   validateTheVisibilityOfHamburgerMenu()
   @allure.step("Validate the visibility of Account & Lists")
   def validateTheVisibilityOfAccountAndLists():
      expect(page.get_by_text("Account & Lists")).not_to_be_visible()
   validateTheVisibilityOfAccountAndLists()
