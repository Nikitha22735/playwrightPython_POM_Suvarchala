import allure
from playwright.sync_api import sync_playwright, expect, Page

class login():
    def __init__(self, page: Page):
        self.emailTextBox = page.locator("#ap_email_login")
        self.continueBtn = page.locator('[type="submit"]')
        self.passwordTextBox = page.locator('#ap_password')

    @allure.step("Enter the email ID in email text box")
    def enterEmail(self, emailID):
        self.emailTextBox.fill(emailID)

    @allure.step("Click on continue button")
    def clickOnContinue(self):
        self.continueBtn.click()
    
    @allure.step("Enter the password in password text box")
    def enterPw(self, pw):
        self.passwordTextBox.fill(pw)
