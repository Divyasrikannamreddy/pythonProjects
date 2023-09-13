from selenium import webdriver
driver = webdriver.Chrome()
driver =webdriver.Edge()
driver.get("https://www.google.co.in/")
driver.maximize_window()
driver.close()