import time

import pytest
from selenium import webdriver



@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(3)
    request.cls.driver=driver
    yield
    driver.close()
