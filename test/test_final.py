import time

import pytest
from selenium.webdriver import ActionChains, Keys

from pageobject import reject
from pageobject.Loginpage import LoginPage
from pageobject.Recruitment import Recruitment
from pageobject.RejectCandidate import RejectCandidate
#from pageobject.reject import Reject


@pytest.mark.usefixtures("setup")
class Testone:
    def testfinal(self):
        loginpage = LoginPage(self.driver)
        #time.sleep(3)
        loginpage.getName().send_keys("Admin")
        #time.sleep(2)
        loginpage.getPassword().send_keys("admin123")
        #time.sleep(2)
        loginpage.getLogin().click()
        time.sleep(2)
        recruitmentpg = Recruitment(self.driver)
        recruitmentpg.getRecruit().click()
        time.sleep(2)
        recruitmentpg.getVacancy().click()
        actions = ActionChains(self.driver)
        actions.send_keys("s")
        time.sleep(2)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        #actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)

        recruitmentpg.getStatus().click()

        actions2 = ActionChains(self.driver)
        actions2.send_keys("s")
        #actions2.send_keys(Keys.ARROW_DOWN)
        actions2.send_keys(Keys.ENTER)
        time.sleep(2)
        actions2.perform()
        time.sleep(3)
        recruitmentpg.getSearchbtn().click()
        time.sleep(2)

        #countlist = recruitmentpg.getcount()
        #c=0
        #for short in countlist:
            #if short == "Shortlisted":
        #print(len(countlist))
            #c+=1
            #print(l)
        #time.sleep(3)

        recruitmentpg.getEye().click()
        time.sleep(2)

        Rejectbtn = reject(self.driver)
        Rejectbtn.getRejectbt().click()

        candidate=RejectCandidate(self.driver)
        candidate.getrejectcandidate().click()


