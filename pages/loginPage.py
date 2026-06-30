from playwright.sync_api import sync_playwright, expect, Page

class login():
    def __init__(self, page: Page):
        self.emailTextBox = page.locator("#ap_email_login")
        self.continueBtn = page.locator('[type="submit"]')
        self.passwordTextBox = page.locator('#ap_password')


    def enterEmail(self, emailID):
        self.emailTextBox.fill(emailID)

    def clickOnContinue(self):
        self.continueBtn.click()

    def enterPw(self, pw):
        self.passwordTextBox.fill(pw)
