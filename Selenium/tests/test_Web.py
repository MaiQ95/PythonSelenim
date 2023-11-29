#import base packages
import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

#import expension of packages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import from project
from utilities.BaseClass import BaseClass
from pageObjects.Web import Web
from TestData.WebData import WebData


class TestOne(BaseClass):

    def test_web(self, getData):
        self.driver.get("http://sitename.com")

        #Change
        web = Web(self.driver)

        #Wait for browser
        self.driver.implicitly_wait(1800)
        wait = WebDriverWait(self.driver, 10)

        time.sleep(2)

        #Get element By ID
        wait.until(EC.visibility_of_element_located((By.ID, "type_element_ID")))
        trendwatch.getElementByID().click()

        time.sleep(5)

        #Handle dropdown
        web.getDropdownBtn().click()
        time.sleep(3)
        dropdownElements = web.getDropdownElements()
        time.sleep(3)
        for element in dropdownElements:
            if element.text == getData["DropdownSearch"]:
                element.click()
                break


        time.sleep(2)
        print("Test Passed")


    @pytest.fixture(params = TrendwatchData.test_Trendwatch_data)
    def getData(self, request):
        return request.param
