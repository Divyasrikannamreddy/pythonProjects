from selenium.webdriver.common.by import By

class RejectCandidate:
    def __init__(self,driver):
        self.driver = driver

    candidate=(By.CSS_SELECTOR,"button[class*='orangehrm-left-space']")


    def getrejectcandidate(self):
        return self.driver.find_element(*RejectCandidate.candidate)