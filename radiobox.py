import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").is_selected()
time.sleep(3)

