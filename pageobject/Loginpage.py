from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self,driver):
        self.driver = driver


    loginname = (By.CSS_SELECTOR,"input[name='username']")
    password = (By.CSS_SELECTOR,"input[name='password']")
    login = (By.XPATH,"//button[@type='submit']")


    def getName(self):
        return self.driver.find_element(*LoginPage.loginname)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLogin(self):
        return self.driver.find_element(*LoginPage.login)


