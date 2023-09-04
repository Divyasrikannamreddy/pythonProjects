from selenium.webdriver.common.by import By


class Recruitment:
    recruit=(By.XPATH,"//a[contains(@href,'RecruitmentModule')]")
    vacancy=
    status=
    search=(By.CSS_SELECTOR,"button[type='submit']")

    def getRecruit(self):
        return self.driver.find_element(*Recruitment.recruit)

    def getVacancy(self):
        return self.driver.find_element(*Recruitment.vacancy)

    def getStatus(self):
        return self.driver.find_element(*Recruitment.status)

    def getSearch(self):
        return self.driver.find_element(*Recruitment.search)