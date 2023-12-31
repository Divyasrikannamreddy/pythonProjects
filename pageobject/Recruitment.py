from selenium.webdriver.common.by import By


class Recruitment:
    def __init__(self, driver):
        self.driver = driver
    recruit = (By.XPATH, "//a[contains(@href,'recruitment')]")
    vacancy = (By.XPATH, ("(//i[contains(@class,'oxd-select-text--arrow')])[2]"))
    status = (By.XPATH, "(//i[contains(@class,'oxd-select-text--arrow')])[4]")
    search = (By.XPATH, "//button[@type='submit']")
    #compare=(By.XPATH,"//div[contains(@class,'orangehrm-horizontal')]/span")
    #count=(By.XPATH,"//div[text()='Shortlisted']")
    ct=(By.XPATH,"//div[@role='row']")
    record=(By.XPATH,"//div[contains(@class,'orangehrm-horizontal-padding')]/span")
    #vacancy1=(By.XPATH,"//div[text()='Software Engineer']")
    eye=(By.XPATH,"(//i[contains(@class,'icon bi-eye-fill')][1])")

    def getRecruit(self):
        return self.driver.find_element(*Recruitment.recruit)


    def getVacancy(self):
        return self.driver.find_element(*Recruitment.vacancy)

    def getStatus(self):
        return self.driver.find_element(*Recruitment.status)

    def getSearchbtn(self):
        return self.driver.find_element(*Recruitment.search)

    '''def getcount(self):
        return self.driver.find_elements(*Recruitment.count)'''

    '''def getVacancy1(self):
        return self.driver.find_elements(*Recruitment.vacancy1)

    def getEye(self):
        return self.driver.find_elements(*Recruitment.eye)'''

    def getCt(self):
        return self.driver.find_elements(*Recruitment.ct)

    def getRecord(self):
        return self.driver.find_element(*Recruitment.record)

    def getEye(self):
        return self.driver.find_element(*Recruitment.eye)