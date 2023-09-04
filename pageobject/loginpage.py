from selenium.webdriver.common.by import By



class loginpage:
    def __init__(self,driver):


    loginname=(By.CSS_SELECTOR,"input[name='username']")
    password=(By.CSS_SELECTOR,"input[name='password']")
    login=(By.CSS_SELECTOR,"button[type='submit']")


    def getName(self):
        return self.driver.find_element(*loginpage.loginname)

    def getPassword(self):
        return self.driver.find_element(*loginpage.password)

    def getLogin(self):
        return self.driver.find_element(*loginpage.login)


