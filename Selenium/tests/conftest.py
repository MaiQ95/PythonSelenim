#import base packages
import pytest
from selenium import webdriver
import time


#import expension of packages
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service


#Set browser to all selenium operation (Selected - Edge)
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        #Set chrome service and webdriver path
        print("chrome")
    elif browser_name == "firefox":
        #Set firefox service and webdriver path
        print("firefox")
    elif browser_name == "edge":
        service_obj = Service()
        #Set browser service
        service_obj = Service("C:/Users/.../msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)


    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
