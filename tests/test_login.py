from pages.homePage import home
from pages.loginPage import login


def test_positiveLogin(page, naviagetToBrowser):
    homePageObj = home(page)
    homePageObj.clickOnAccountsNdList()
    loginPageObj = login(page)
    loginPageObj.enterEmail("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinue()
    loginPageObj.enterPw("Welcome@04")
    loginPageObj.clickOnContinue()
    homePageObj.validateTheVisibityOfSearchBox()


    