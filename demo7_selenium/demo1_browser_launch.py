import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
time.sleep((10))