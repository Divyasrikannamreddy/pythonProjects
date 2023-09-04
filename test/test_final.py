import pytest
from pageobject.loginpage import loginpage

class Testone:
    def test_sample(self):
        LoginPage=loginpage(self,driver)
        LoginPage.getName().send_keys("Admin")
        LoginPage.getPassword().send_keys("admin123")
        LoginPage.getLogin().click()
