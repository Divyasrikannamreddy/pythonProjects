
from selenium.webdriver.common.by import By


class reject:
    def __init__(self,driver):
        self.driver = driver
    rejectbt = (By.XPATH,"//button[contains(@class,'danger')]")

    def getRejectbt(self):
        return self.driver.find_element(*reject.rejectbt)
