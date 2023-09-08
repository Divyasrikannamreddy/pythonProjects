from selenium.webdriver.common.by import By


class FinalCandidates:
    def __init__(self,driver):
        self.driver = driver

    candidate = (By.XPATH, "(//a[contains(@href,'#')])[1]")
    vacancy1 = (By.XPATH, ("(//i[contains(@class,'oxd-select-text--arrow')])[2]"))
    status1 = (By.XPATH, "(//i[contains(@class,'oxd-select-text--arrow')])[4]")
    #search1 = (By.XPATH, "//button[text()=' Search ']")
    #ct1 = (By.XPATH, "//div[@role='row']")
    #record1 = (By.XPATH, "//div[contains(@class,'orangehrm-horizontal-padding')]/span")

    def getCandidate(self):
        return self.driver.find_element(*FinalCandidates.candidate)

    def getVacancy1(self):
        return self.driver.find_element(*FinalCandidates.vacancy1)

    def getStatus1(self):
        return self.driver.find_element(*FinalCandidates.status1)

    #def getSearchbtn1(self):
        #return self.driver.find_element(*FinalCandidates.search1)

    #def getct1(self):
        #return self.driver.find_element(*FinalCandidates.ct1)

    #def getrecord1(self):
        #return self.driver.find_element(*FinalCandidates.record1)
