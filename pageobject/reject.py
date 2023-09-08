
from selenium.webdriver.common.by import By


class Reject:
    def __init__(self,driver):
        self.driver = driver
    rejectbt = (By.XPATH,"//button[contains(@class,'danger')]")
    save=(By.CLASS_NAME,"orangehrm-left-space")

    def getRejectbt(self):
        return self.driver.find_element(*Reject.rejectbt)

    def getSave(self):
        return self.driver.find_element(*Reject.save)
