from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element (By.CSS_SELECTOR, "input[name='username']").send_keys("Admin")
driver.find_element (By.CSS_SELECTOR, "input[name='password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
action=ActionChains(driver)