import logging
import time

import pytest
from selenium.webdriver import ActionChains, Keys

from pageobject import reject
from pageobject.Baseclass import Baseclass
from pageobject.Loginpage import LoginPage
from pageobject.Recruitment import Recruitment

from pageobject.RejectCandidate import RejectCandidate
from pageobject.finalcandidates import FinalCandidates
from pageobject.reject import Reject


#from pageobject.reject import Reject


class Testone(Baseclass):

    def testfinal(self):
        log=self.getLogger()
        log.info("i am in login page")
        loginpage = LoginPage(self.driver)
        #time.sleep(3)
        loginpage.getName().send_keys("Admin")
        #time.sleep(2)
        loginpage.getPassword().send_keys("admin123")
        #time.sleep(2)
        loginpage.getLogin().click()
        time.sleep(2)
        recruitmentpg1 = Recruitment(self.driver)
        recruitmentpg1.getRecruit().click()
        time.sleep(2)
        recruitmentpg1.getVacancy().click()
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

        recruitmentpg1.getStatus().click()

        actions2 = ActionChains(self.driver)
        actions2.send_keys("s")
        #actions2.send_keys(Keys.ARROW_DOWN)
        actions2.send_keys(Keys.ENTER)
        time.sleep(2)
        actions2.perform()
        time.sleep(3)
        recruitmentpg1.getSearchbtn().click()
        time.sleep(2)
        log.info("count the legth of candidates")
#getting shortlisted count

        for shortlist in recruitmentpg1.getCt():
            if "Shorlisted" and "Software Engineer" in shortlist.text:
                pass


        time.sleep(3)
        rec = recruitmentpg1.getRecord().text
        print(rec)



        recruitmentpg1.getEye().click()
        time.sleep(2)

        rejectbtn = Reject(self.driver)
        rejectbtn.getRejectbt().click()
        time.sleep(2)
        rejectbtn.getSave().click()
        time.sleep(2)


        Candidate=FinalCandidates(self.driver)
        Candidate.getCandidate().click()
        time.sleep(2)

        Finalcandidate=FinalCandidates(self.driver)
        Finalcandidate.getVacancy1().click()
        actions3 = ActionChains(self.driver)
        actions3.send_keys("s")
        time.sleep(5)
        actions3.send_keys(Keys.ARROW_DOWN)
        actions3.send_keys(Keys.ARROW_DOWN)
        actions3.send_keys(Keys.ARROW_DOWN)
        # actions.send_keys(Keys.ARROW_DOWN)
        actions3.send_keys(Keys.ENTER)
        actions3.perform()
        time.sleep(2)
        Finalcandidate.getStatus1().click()

        actions4 = ActionChains(self.driver)
        actions4.send_keys("s")
        # actions2.send_keys(Keys.ARROW_DOWN)
        actions4.send_keys(Keys.ENTER)
        time.sleep(2)
        actions4.perform()
        time.sleep(3)
        recruitmentpg1.getSearchbtn().click()
        time.sleep(5)

#after rejection shortlisted count

        for shortlist in recruitmentpg1.getCt():
            if "Shorlisted" and "Software Engineer" in shortlist.text:
                pass

        time.sleep(3)
        rec = recruitmentpg1.getRecord().text
        print(rec)

