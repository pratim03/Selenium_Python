import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUeseName()
    password = ReadConfig.getPassword()


    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title

        if actual_title == "Your store. Login1":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_text = self.driver.title

        if actual_text == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            assert False
