import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUeseName()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()
    def test_homePageTitle(self, setup):
        self.logger.info("******************* Test_001_Login **********************")
        self.logger.info("******************* Verifying Homepage Test Case **********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        actual_title = self.driver.title

        if actual_title == "Your store. Login1":
            assert True
            self.logger.info("*******************  Homepage Test Case Passed **********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homePageTitle.png")
            self.logger.warning("*******************  Homepage Test Case Failed **********************")
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
            self.logger.info("*******************  Login Test Case Passed **********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.logger.warning("*******************  Login Test Case Failed **********************")
            self.driver.close()
            assert False
