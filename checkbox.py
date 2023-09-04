from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"input[value='option2']").click()
driver.find_element(By.CSS_SELECTOR,"input[value='option3']").click()