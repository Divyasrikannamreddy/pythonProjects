import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.in/")
textbox=driver.find_element(By.ID,"APjFqb")
textbox.send_keys("flowers")
time.sleep(5)