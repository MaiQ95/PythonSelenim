from selenium.webdriver.common.by import By

class Web:

    def __init__(self, driver):
        self.driver = driver


    #write all selectors on this page

    #set by ID
    setID = (By.ID, "type_element_ID")
    #Set by XPATH
    dropdownBtn = (By.XPATH, "type_element_XPATH")
    dropdownElements = (By.XPATH, "type_element_XPATH")


    #Language handle
    def getElementByID(self):
        return self.driver.find_element(*Web.setID)

    #Line handle
    def getDropdownBtn(self):
        return self.driver.find_element(*Web.dropdownBtn)

    def getDropdownElements(self):
        return self.driver.find_element(*Web.dropdownElements)
