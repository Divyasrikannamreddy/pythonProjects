import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.co.in/")
time.sleep(2)
'''print("title-"+driver.title)
print("browsername-"+driver.name)'''