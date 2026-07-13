# searchbox = page.locator("input#twotabsearchtextbox")
import allure
from playwright.sync_api import sync_playwright, expect, Page
class home:
    def __init__(self, page: Page):
        self.searchbox = page.locator("input#twotabsearchtextbox")
        self.searchicon = page.locator("#nav-search-submit-button")
        self.accountsNdList = page.get_by_text("Account & Lists")

    @allure.step("enterProductInSearchBox")
    def enterProductInSearchBox(self, product):
        self.searchbox.fill(product)

    @allure.step("Click on search button")
    def clickOnSearchBtn(self):
        self.searchicon.click()


    @allure.step("Validate the visibility of search box")
    def validateTheVisibityOfSearchBox(self):
        expect(self.searchbox).to_be_visible()

    @allure.step("Click on Account & Lists")
    def clickOnAccountsNdList(self):
        self.accountsNdList.click()