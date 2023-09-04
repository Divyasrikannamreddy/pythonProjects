from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
Select=select(driver.find_element(By.ID,"dropdown-class-example"))
Select.select_by_Visible_Text("Option2")
