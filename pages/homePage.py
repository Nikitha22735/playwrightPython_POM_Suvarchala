# searchbox = page.locator("input#twotabsearchtextbox")
from playwright.sync_api import sync_playwright, expect
class home:
    def __init__(self, page):
        self.searchbox = page.locator("input#twotabsearchtextbox")
        self.searchicon = page.locator("#nav-search-submit-button")

    def enterProductInSearchBox(self, product):
        self.searchbox.fill(product)

    def clickOnSearchBtn(self):
        self.searchicon.click()


    def validateTheVisibityOfSearchBox(self):
        expect(self.searchbox).to_be_visible()